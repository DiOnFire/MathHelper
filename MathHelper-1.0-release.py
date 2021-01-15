from tkinter import *
from tkinter.ttk import Combobox
import time
import sys
from abc import ABCMeta, abstractmethod
import json
import logging
import os
import socket
import struct
import uuid
import threading
import re

OP_HANDSHAKE = 0
OP_FRAME = 1
OP_CLOSE = 2
OP_PING = 3
OP_PONG = 4

logger = logging.getLogger(__name__)


class DiscordIpcError(Exception):
    pass


class DiscordIpcClient(metaclass=ABCMeta):

    """Work with an open Discord instance via its JSON IPC for its rich presence API.

    In a blocking way.
    Classmethod `for_platform`
    will resolve to one of WinDiscordIpcClient or UnixDiscordIpcClient,
    depending on the current platform.
    Supports context handler protocol.
    """

    def __init__(self, client_id):
        self.client_id = client_id
        self._connect()
        self._do_handshake()
        logger.info("connected via ID %s", client_id)

    @classmethod
    def for_platform(cls, client_id, platform=sys.platform):
        if platform == 'win32':
            return WinDiscordIpcClient(client_id)
        else:
            return UnixDiscordIpcClient(client_id)

    @abstractmethod
    def _connect(self):
        pass

    def _do_handshake(self):
        ret_op, ret_data = self.send_recv({'v': 1, 'client_id': self.client_id}, op=OP_HANDSHAKE)
        # {'cmd': 'DISPATCH', 'data': {'v': 1, 'config': {...}}, 'evt': 'READY', 'nonce': None}
        if ret_op == OP_FRAME and ret_data['cmd'] == 'DISPATCH' and ret_data['evt'] == 'READY':
            return
        else:
            if ret_op == OP_CLOSE:
                self.close()
            raise RuntimeError(ret_data)

    @abstractmethod
    def _write(self, date: bytes):
        pass

    @abstractmethod
    def _recv(self, size: int) -> bytes:
        pass

    def _recv_header(self) -> (int, int):
        header = self._recv_exactly(8)
        return struct.unpack("<II", header)

    def _recv_exactly(self, size) -> bytes:
        buf = b""
        size_remaining = size
        while size_remaining:
            chunk = self._recv(size_remaining)
            buf += chunk
            size_remaining -= len(chunk)
        return buf

    def close(self):
        logger.warning("closing connection")
        try:
            self.send({}, op=OP_CLOSE)
        finally:
            self._close()

    @abstractmethod
    def _close(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()

    def send_recv(self, data, op=OP_FRAME):
        self.send(data, op)
        return self.recv()

    def send(self, data, op=OP_FRAME):
        logger.debug("sending %s", data)
        data_str = json.dumps(data, separators=(',', ':'))
        data_bytes = data_str.encode('utf-8')
        header = struct.pack("<II", op, len(data_bytes))
        self._write(header + data_bytes)

    def recv(self) -> (int, "JSON"):
        """Receives a packet from discord.

        Returns op code and payload.
        """
        op, length = self._recv_header()
        payload = self._recv_exactly(length)
        data = json.loads(payload.decode('utf-8'))
        logger.debug("received %s", data)
        return op, data

    def set_activity(self, act):
        # act
        data = {
            'cmd': 'SET_ACTIVITY',
            'args': {'pid': os.getpid(),
                     'activity': act},
            'nonce': str(uuid.uuid4())
        }
        self.send(data)


class WinDiscordIpcClient(DiscordIpcClient):

    _pipe_pattern = R'\\?\pipe\discord-ipc-{}'

    def _connect(self):
        for i in range(10):
            path = self._pipe_pattern.format(i)
            try:
                self._f = open(path, "w+b")
            except OSError as e:
                logger.error("failed to open {!r}: {}".format(path, e))
            else:
                break
        else:
            return DiscordIpcError("Failed to connect to Discord pipe")

        self.path = path

    def _write(self, data: bytes):
        self._f.write(data)
        self._f.flush()

    def _recv(self, size: int) -> bytes:
        return self._f.read(size)

    def _close(self):
        self._f.close()


class UnixDiscordIpcClient(DiscordIpcClient):

    def _connect(self):
        self._sock = socket.socket(socket.AF_UNIX)
        pipe_pattern = self._get_pipe_pattern()

        for i in range(10):
            path = pipe_pattern.format(i)
            if not os.path.exists(path):
                continue
            try:
                self._sock.connect(path)
            except OSError as e:
                logger.error("failed to open {!r}: {}".format(path, e))
            else:
                break
        else:
            return DiscordIpcError("Failed to connect to Discord pipe")

    @staticmethod
    def _get_pipe_pattern():
        env_keys = ('XDG_RUNTIME_DIR', 'TMPDIR', 'TMP', 'TEMP')
        for env_key in env_keys:
            dir_path = os.environ.get(env_key)
            if dir_path:
                break
        else:
            dir_path = '/tmp'
        return os.path.join(dir_path, 'discord-ipc-{}')

    def _write(self, data: bytes):
        self._sock.sendall(data)

    def _recv(self, size: int) -> bytes:
        return self._sock.recv(size)

    def _close(self):
        self._sock.close()


# Дэфолтные настройки
config = {
    "background": "#FFFFFF",
    "background_text": "#FFFFFF",
    "foreground_text": "#000000",
    "background_button": "#FFFFFF",
    "foreground_button": "#000000",
    "background_entry": "#FFFFFF"
}


default_config = {
    "background": "#FFFFFF",
    "background_text": "#FFFFFF",
    "foreground_text": "#000000",
    "background_button": "#FFFFFF",
    "foreground_button": "#000000",
    "background_entry": "#FFFFFF"
}


# Словарь с данными для дискорд рпц
activity = {
    "state": "Версия v1.0-beta (dev)",
    "details": "В главном меню",
    "assets": {
        "large_text": "MathHelper",
        "large_image": "icon"
    }
}


def config_load():
    with open("config.json", "r") as file:
        data = json.load(file)
    return data


def is_correct_hex(hex):
    check = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hex)
    if check:
        return 1
    else:
        return 0


def close():
    sys.exit(0)


def discord_rpc():
    global client_id
    client_id = '797139388513386546'
    rpc_obj = DiscordIpcClient.for_platform(client_id)
    print("RPC connection successful.")
    time.sleep(5)
    while True:
        rpc_obj.set_activity(activity)
        time.sleep(5)


def Perimetr():
    activity["details"] = "Рассчитывает периметр"
    data = config_load()

    def perimeter_clicked():
        try:
            float(shirina.get())
            float(dlina.get())
        except ValueError:
            error_window = Tk()
            error_window["bg"] = data["background"]
            error_window.title("Ошибка!")
            error_window.geometry('400x250')
            error = Label(error_window, text="Введите корректные данные!",
                          bg=data["background_text"], fg=data["foreground_text"])
            error.grid(column=0, row=0)
            error_window.mainloop()
        else:
            if shirina.get() > dlina.get():  # If contradiction
                error_window = Tk()
                error_window["bg"] = data["background"]
                error_window.title("Ошибка!")
                error_window.geometry('400x250')
                error = Label(error_window, text="Ошибка: ширина не может быть больше длины. Повторите попытку!", bg=data["background_text"], fg=data["foreground_text"])
                error.grid(column=0, row=0)
                error_window.mainloop()
            elif shirina.get().isdigit() is False or dlina.get().isdigit() is False:
                error_window = Tk()
                error_window["bg"] = data["background"]
                error_window.title("Ошибка!")
                error_window.geometry('400x250')
                error = Label(error_window, text="Введите корректные данные!",
                              bg=data["background_text"], fg=data["foreground_text"])
                error.grid(column=0, row=0)
                error_window.mainloop()
            elif shirina.get() < dlina.get() or shirina.get() == dlina.get():  # Getting perimeter
                result_window = Tk()
                result_window["bg"] = data["background"]
                result_window.title("Результат")
                result_window.geometry('250x150')
                rezyltat_perimetr = float(dlina.get()) + float(shirina.get()) + float(dlina.get()) + float(shirina.get())
                final = "Периметр равен " + str(rezyltat_perimetr)
                result = Label(result_window, text=final, bg=data["background_text"], fg=data["foreground_text"])
                result.grid(column=1, row=0)
                result_window.mainloop()

    def clicked():
        activity["details"] = "В главном меню"
        perimeter_window.destroy()

    perimeter_window = Tk()
    perimeter_window["bg"] = data["background"]
    perimeter_window.resizable(width=False, height=False)
    perimeter_window.title("MathHelper - Периметр")
    perimeter_window.geometry('832x300')
    warning = Label(perimeter_window,
                    text="ВНИМАНИЕ! Если вам нужно ввести десятичную дробь, то используйте ТОЧКУ для разделения целой и десятичной части!", bg=data["background_text"], fg=data["foreground_text"])
    warning.grid(column=0, row=0)
    text = Label(perimeter_window, text="Введите ширину", bg=data["background_text"], fg=data["foreground_text"])
    text.grid(column=0, row=1)
    shirina = Entry(perimeter_window, width=10, bg=data["background_entry"], fg=data["foreground_text"])
    shirina.grid(column=0, row=2)
    text1 = Label(perimeter_window, text="Введите длину", bg=data["background_text"], fg=data["foreground_text"])
    text1.grid(column=0, row=3)
    dlina = Entry(perimeter_window, width=10, bg=data["background_entry"], fg=data["foreground_text"])
    dlina.grid(column=0, row=4)
    ok_button = Button(perimeter_window, text="Oк!", command=perimeter_clicked, bg=data["background_button"], fg=data["foreground_button"])
    ok_button.grid(column=0, row=5)
    button_close = Button(perimeter_window, text="Закрыть", command=clicked, bg=data["background_button"], fg=data["foreground_button"])
    button_close.grid(column=0, row=6)
    perimeter_window.mainloop()


def Ploshad():
    activity["details"] = "Рассчитывает площадь"
    data = config_load()

    def area_clicked():
        try:
            float(shirina.get())
            float(dlina.get())
        except ValueError:
            error_window = Tk()
            error_window["bg"] = data["background"]
            error_window.title("Ошибка!")
            error_window.geometry('400x250')
            error = Label(error_window, text="Введите корректные данные!",
                          bg=data["background_text"], fg=data["foreground_text"])
            error.grid(column=0, row=0)
            error_window.mainloop()
        else:
            result_window_area = Tk()
            result_window_area["bg"] = data["background"]
            rezyltat_ploshad = int(dlina.get()) * int(shirina.get())
            result_window_area.title("Результат")
            result_window_area.geometry('250x150')
            final = "Площадь равна " + str(rezyltat_ploshad)
            result = Label(result_window_area, text=final, bg=data["background_text"], fg=data["foreground_text"])
            result.grid(column=1, row=0)
            result_window_area.mainloop()

    def clicked():
        activity["details"] = "В главном меню"
        area_window.destroy()
    area_window = Tk()
    area_window["bg"] = data["background"]
    area_window.resizable(width=False, height=False)
    area_window.title("MathHelper - Площадь")
    area_window.geometry('832x300')
    warning = Label(area_window,
                    text="ВНИМАНИЕ! Если вам нужно ввести десятичную дробь, то используйте ТОЧКУ для разделения целой и десятичной части!", bg=data["background_text"], fg=data["foreground_text"])
    warning.grid(column=0, row=0)
    text = Label(area_window, text="Введите ширину", bg=data["background_text"], fg=data["foreground_text"])
    text.grid(column=0, row=1)
    shirina = Entry(area_window, width=10, bg=data["background_entry"])
    shirina.grid(column=0, row=2)
    text1 = Label(area_window, text="Введите длину", bg=data["background_text"], fg=data["foreground_text"])
    text1.grid(column=0, row=3)
    dlina = Entry(area_window, width=10, bg=data["background_entry"])
    dlina.grid(column=0, row=4)
    ok_button = Button(area_window, text="Oк!", command=area_clicked, bg=data["background_button"], fg=data["foreground_button"])
    ok_button.grid(column=0, row=5)
    button_close = Button(area_window, text="Закрыть", command=clicked, bg=data["background_button"], fg=data["foreground_button"])
    button_close.grid(column=0, row=6)
    area_window.mainloop()


def Obyem():
    activity["details"] = "Рассчитывает объем"
    data = config_load()

    def void_clicked():
        try:
            float(shirina.get())
            float(dlina.get())
            float(length.get())
        except ValueError:
            error_window = Tk()
            error_window["bg"] = data["background"]
            error_window.title("Ошибка!")
            error_window.geometry('400x250')
            error = Label(error_window, text="Введите корректные данные!",
                          bg=data["background_text"], fg=data["foreground_text"])
            error.grid(column=0, row=0)
            error_window.mainloop()
        else:
            if float(shirina.get()) < 0 or float(dlina.get()) < 0 or float(length.get()) < 0:
                error_window = Tk()
                error_window["bg"] = data["background"]
                error_window.title("Ошибка!")
                error_window.geometry('400x250')
                error = Label(error_window, text="Ошибка: значения не моут меньше нуля. Повторите попытку!", bg=data["background_text"], fg=data["foreground_text"])
                error.grid(column=0, row=0)
                error_window.mainloop()
            else:
                result_window = Tk()
                result_window["bg"] = data["background"]
                result_window.title("Результат")
                result_window.geometry('250x150')
                result = float(dlina.get()) * float(shirina.get()) * float(length.get())
                final = "Объем равен " + str(result)
                result = Label(result_window, text=final, bg=data["background_text"], fg=data["foreground_text"])
                result.grid(column=1, row=0)
                result_window.mainloop()

    def clicked():
        activity["details"] = "В главном меню"
        void_window.destroy()
    void_window = Tk()
    void_window["bg"] = data["background"]
    void_window.resizable(width=False, height=False)
    void_window.title("MathHelper - Площадь")
    void_window.geometry('832x300')
    warning = Label(void_window,
                    text="ВНИМАНИЕ! Если вам нужно ввести десятичную дробь, то используйте ТОЧКУ для разделения целой и десятичной части!", bg=data["background_text"], fg=data["foreground_text"])
    warning.grid(column=0, row=0)
    text = Label(void_window, text="Введите ширину", bg=data["background_text"], fg=data["foreground_text"])
    text.grid(column=0, row=1)
    shirina = Entry(void_window, width=10, bg=data["background_entry"])
    shirina.grid(column=0, row=2)
    text1 = Label(void_window, text="Введите длину", bg=data["background_text"], fg=data["foreground_text"])
    text1.grid(column=0, row=3)
    dlina = Entry(void_window, width=10, bg=data["background_entry"])
    dlina.grid(column=0, row=4)
    text2 = Label(void_window, text="Введите высоту", bg=data["background_text"], fg=data["foreground_text"])
    text2.grid(column=0, row=5)
    length = Entry(void_window, width=10, bg=data["background_entry"])
    length.grid(column=0, row=6)
    ok_button = Button(void_window, text="Oк!", command=void_clicked, bg=data["background_button"], fg=data["foreground_button"])
    ok_button.grid(column=0, row=7)
    button_close = Button(void_window, text="Закрыть", command=clicked, bg=data["background_button"], fg=data["foreground_button"])
    button_close.grid(column=0, row=8)
    void_window.mainloop()


def Konverter_velichin():
    def clicked():
        is_complete = True
        try:
            float(data_value.get())
        except ValueError:
            error_window = Tk()
            error_window["bg"] = data["background"]
            error_window.title("Ошибка!")
            error_window.geometry('400x250')
            error = Label(error_window, text="Введите корректные данные!",
                          bg=data["background_text"], fg=data["foreground_text"])
            error.grid(column=0, row=0)
            error_window.mainloop()
        else:
            if first_value.get() == "Сантиметры" and second_value.get() == "Сантиметры":
                answer = float(data_value.get())
            elif first_value.get() == "Метры" and second_value.get() == "Сантиметры":
                answer = float(data_value.get()) * 100
            elif first_value.get() == "Миллиметры" and second_value.get() == "Сантиметры":
                answer = float(data_value.get()) / 10
            elif first_value.get() == "Километры" and second_value.get() == "Сантиметры":
                answer = float(data_value.get()) * 1000000
            elif first_value.get() == "Дециметры" and second_value.get() == "Сантиметры":
                answer = float(data_value.get()) * 10
            elif first_value.get() == "Сантиметры" and second_value.get() == "Миллиметры":
                answer = float(data_value.get()) * 10
            elif first_value.get() == "Метры" and second_value.get() == "Миллиметры":
                answer = float(data_value.get()) * 1000
            elif first_value.get() == "Миллиметры" and second_value.get() == "Миллиметры":
                answer = float(data_value.get())
            elif first_value.get() == "Километры" and second_value.get() == "Миллиметры":
                answer = float(data_value.get()) * 10000000
            elif first_value.get() == "Дециметры" and second_value.get() == "Миллиметры":
                answer = float(data_value.get()) * 100
            elif first_value.get() == "Сантиметры" and second_value.get() == "Метры":
                answer = float(data_value.get()) / 100
            elif first_value.get() == "Метры" and second_value.get() == "Метры":
                answer = float(data_value.get())
            elif first_value.get() == "Миллиметры" and second_value.get() == "Метры":
                answer = float(data_value.get()) / 1000
            elif first_value.get() == "Километры" and second_value.get() == "Метры":
                answer = float(data_value.get()) / 1000
            elif first_value.get() == "Дециметры" and second_value.get() == "Метры":
                answer = float(data_value.get()) / 10
            elif first_value.get() == "Сантиметры" and second_value.get() == "Дециметры":
                answer = float(data_value.get()) / 10
            elif first_value.get() == "Метры" and second_value.get() == "Дециметры":
                answer = float(data_value.get()) / 10
            elif first_value.get() == "Миллиметры" and second_value.get() == "Дециметры":
                answer = float(data_value.get()) / 10
            elif first_value.get() == "Километры" and second_value.get() == "Дециметры":
                answer = float(data_value.get()) / 10
            elif first_value.get() == "Дециметры" and second_value.get() == "Дециметры":
                answer = float(data_value.get())
            elif first_value.get() == "Сантиметры" and second_value.get() == "Километры":  # kilometri
                answer = float(data_value.get()) / 1000000
            elif first_value.get() == "Метры" and second_value.get() == "Километры":
                answer = float(data_value.get()) / 1000
            elif first_value.get() == "Миллиметры" and second_value.get() == "Километры":
                answer = float(data_value.get()) / 10000000
            elif first_value.get() == "Километры" and second_value.get() == "Километры":
                answer = float(data_value.get())
            elif first_value.get() == "Дециметры" and second_value.get() == "Километры":
                answer = float(data_value.get()) / 100
            elif first_value.get() == "Граммы" and second_value.get() == "Граммы":
                answer = float(data_value.get())
            elif first_value.get() == "Граммы" and second_value.get() == "Килограммы":
                answer = float(data_value.get()) / 1000
            elif first_value.get() == "Граммы" and second_value.get() == "Цейнтнеры":
                answer = float(data_value.get()) / 100000
            elif first_value.get() == "Граммы" and second_value.get() == "Тонны":
                answer = float(data_value.get()) / 1000000
            elif first_value.get() == "Килограммы" and second_value.get() == "Граммы":
                answer = float(data_value.get()) * 1000
            elif first_value.get() == "Килограммы" and second_value.get() == "Килограммы":
                answer = float(data_value.get())
            elif first_value.get() == "Килограммы" and second_value.get() == "Цейнтнеры":
                answer = float(data_value.get()) / 100
            elif first_value.get() == "Килограммы" and second_value.get() == "Тонны":
                answer = float(data_value.get()) / 1000
            elif first_value.get() == "Цейнтнеры" and second_value.get() == "Граммы":
                answer = float(data_value.get()) * 100000
            elif first_value.get() == "Цейнтнеры" and second_value.get() == "Килограммы":
                answer = float(data_value.get()) * 100
            elif first_value.get() == "Цейнтнеры" and second_value.get() == "Цейнтнеры":
                answer = float(data_value.get())
            elif first_value.get() == "Цейнтнеры" and second_value.get() == "Тонны":
                answer = float(data_value.get()) / 10
            elif first_value.get() == "Тонны" and second_value.get() == "Граммы":
                answer = float(data_value.get()) * 1000000
            elif first_value.get() == "Тонны" and second_value.get() == "Килограммы":
                answer = float(data_value.get()) * 1000
            elif first_value.get() == "Тонны" and second_value.get() == "Цейнтнеры":
                answer = float(data_value.get()) * 10
            elif first_value.get() == "Тонны" and second_value.get() == "Тонны":
                answer = float(data_value.get())
            else:
                is_complete = False
            if is_complete is True:
                result_window = Tk()
                result_window["bg"] = data["background"]
                result_window.title("Результат")
                result_window.geometry('250x150')
                result = float(answer)
                final = "Результат конвертации: " + str(result)
                result = Label(result_window, text=final, bg=data["background_text"], fg=data["foreground_text"])
                result.grid(column=1, row=0)
                result_window.mainloop()
            else:
                error_window = Tk()
                error_window["bg"] = data["background"]
                error_window.title("Ошибка!")
                error_window.geometry('400x250')
                error_window.resizable(height=False, width=False)
                error = Label(error_window, text="Ошибка: невозможно конвертировать величины!",
                              bg=data["background_text"], fg=data["foreground_text"])
                error.grid(column=0, row=0)
                error_window.mainloop()

    def close_window():
        root.destroy()
        activity["details"] = "В главном меню"
    activity["details"] = "Использует конвертер величин"
    data = config_load()
    root = Tk()
    root.geometry('417x379')
    root.resizable(width=False, height=False)
    root.title("MathHelper - Конвертер величин")
    warning = Label(root, text="При вводе дробного числа используйте ТОЧКУ для разделения!", bg=data["background_text"], fg=data["foreground_text"])
    warning.grid(column=0, row=0)
    from_convert = Label(root, text="Из чего переводим", bg=data["background_text"], fg=data["foreground_text"])
    from_convert.grid(column=0, row=1)
    first_value = Combobox(root)
    first_value['values'] = ("Миллиметры", "Сантиметры", "Дециметры", "Метры", "Километры", "Граммы", "Килограммы", "Цейнтнеры", "Тонны")
    first_value.grid(column=0, row=2)
    to_convert = Label(root, text="Во что переводим", bg=data["background_text"], fg=data["foreground_text"])
    to_convert.grid(column=0, row=3)
    second_value = Combobox(root)
    second_value['values'] = ("Миллиметры", "Сантиметры", "Дециметры", "Метры", "Километры", "Граммы", "Килограммы", "Цейнтнеры", "Тонны")
    second_value.grid(column=0, row=4)
    value_text = Label(root, text="Значение величины", bg=data["background_text"], fg=data["foreground_text"])
    value_text.grid(column=0, row=5)
    data_value = Entry(root, width=15)
    data_value.grid(column=0, row=6)
    button = Button(root, text="Ок!", command=clicked, bg=data["background_button"], fg=data["foreground_button"])
    button.grid(column=0, row=7)
    close_button = Button(root, text="Закрыть", command=close_window, bg=data["background_button"], fg=data["foreground_button"])
    close_button.grid(column=0, row=8)
    root.mainloop()


def number_of_digits():
    activity["details"] = "Считает количество цифр в числе"
    data = config_load()

    def clicked():
        if number.get().isdigit():
            result = Tk()
            result.title("Результат")
            result.geometry('272x150')
            final_text = "Вы ввели " + str(len(number.get())) + "- значное число."
            text = Label(result, text=final_text, bg=data["background_text"], fg=data["foreground_text"])
            text.grid(column=0, row=0)
            result.mainloop()
        else:
            error = Tk()
            error.title("Ошибка")
            error.geometry('272x150')
            txt = Label(error, text="Введите корректные данные!", bg=data["background_text"], fg=data["foreground_text"])
            txt.grid(column=0, row=0)
            error.mainloop()

    def close():
        activity["details"] = "В главном меню"
        window.destroy()
    window = Tk()
    window["bg"] = data["background"]
    window.resizable(width=False, height=False)
    window.title("MathHelper - Количество цифр в числе")
    window.geometry('530x180')
    warning = Label(window, text="Для корректной работы программы введите целое и неотрицательное число!", bg=data["background_text"], fg=data["foreground_text"])
    warning.grid(column=0, row=0)
    main_text = Label(window, text="Введите целое число", bg=data["background_text"], fg=data["foreground_text"])
    main_text.grid(column=0, row=1)
    number = Entry(window, width=10, bg=data["background_entry"])
    number.grid(column=0, row=2)
    button = Button(window, text="Ок!", command=clicked, bg=data["background_button"], fg=data["foreground_button"])
    button.grid(column=0, row=3)
    button_close = Button(window, text="Закрыть", command=close, bg=data["background_button"], fg=data["foreground_button"])
    button_close.grid(column=0, row=4)
    window.mainloop()


def get_dividers():
    activity["details"] = "Смотрит делители числа"
    data = config_load()

    def clicked():
        string = ""
        try:
            int(number.get())
        except ValueError:
            error_window = Tk()
            error_window["bg"] = data["background"]
            error_window.title("Ошибка!")
            error_window.geometry('400x250')
            error = Label(error_window, text="Введите корректные данные!",
                          bg=data["background_text"], fg=data["foreground_text"])
            error.grid(column=0, row=0)
            error_window.mainloop()
        else:
            for i in range(1, int(number.get()) + 1):
                if int(number.get()) % i == 0:
                    temp = str(i) + ";"
                    string += temp
            result_window = Tk()
            result_window.geometry('272x150')
            result_window.title("Результат")
            main_text = Label(result_window, text=string, bg=data["background_text"], fg=data["foreground_text"])
            main_text.grid(column=0, row=0)
            result_window.mainloop()

    def closed():
        activity["details"] = "В главном меню"
        root.destroy()

    root = Tk()
    root.title("MathHelper - Делители числа")
    root.resizable(width=False, height=False)
    root.geometry('530x180')
    warning = Label(root, text="Для корректной работы программы введите целое и неотрицательное число!", bg=data["background_text"], fg=data["foreground_text"])
    warning.grid(column=0, row=0)
    txt = Label(root, text="Введите целое число", bg=data["background_text"], fg=data["foreground_text"])
    txt.grid(column=0, row=1)
    number = Entry(root, width=20, bg=data["background_entry"])
    number.grid(column=0, row=2)
    button = Button(root, text="Ок!", command=clicked, bg=data["background_button"], fg=data["foreground_button"])
    button.grid(column=0, row=3)
    button_close = Button(root, text="Закрыть", command=closed, bg=data["background_button"],
                          fg=data["foreground_button"])
    button_close.grid(column=0, row=4)
    root.mainloop()


def simple_number():
    activity["details"] = "Проверяет число"
    data = config_load()

    def clicked():
        try:
            int(number.get())
        except ValueError:
            error_window = Tk()
            error_window["bg"] = data["background"]
            error_window.title("Ошибка!")
            error_window.geometry('400x250')
            error = Label(error_window, text="Введите корректные данные!",
                          bg=data["background_text"], fg=data["foreground_text"])
            error.grid(column=0, row=0)
            error_window.mainloop()
        else:
            is_simple = True
            final_window = Tk()
            final_window.title("Результат")
            final_window.geometry('272x150')
            for i in range(2, int(number.get())):
                if int(number.get()) % i == 0:
                    is_simple = False
                    break
            if is_simple is True:
                final = Label(final_window, text="Введённое число - простое.", bg=data["background_text"], fg=data["foreground_text"])
                final.grid(column=0, row=0)
                final_window.mainloop()
            elif is_simple is False:
                final = Label(final_window, text="Введённое число не является простым.", bg=data["background_text"], fg=data["foreground_text"])
                final.grid(column=0, row=0)
                final_window.mainloop()

    def close():
        activity["details"] = "В главном меню"
        window.destroy()
    window = Tk()
    window["bg"] = data["background"]
    window.resizable(width=False, height=False)
    window.title("MathHelper - Простое число")
    window.geometry('530x180')
    text = Label(window, text="Для корректной работы программы введите целое и неотрицательное число.", bg=data["background_text"], fg=data["foreground_text"])
    text.grid(column=0, row=0)
    txt = Label(window, text="Введите число", bg=data["background_text"], fg=data["foreground_text"])
    txt.grid(column=0, row=1)
    number = Entry(window, width=10, bg=data["background_entry"])
    number.grid(column=0, row=2)
    button = Button(window, text="Ок!", command=clicked, bg=data["background_button"], fg=data["foreground_button"])
    button.grid(column=0, row=3)
    button_close = Button(window, text="Закрыть", command=close, bg=data["background_button"], fg=data["foreground_button"])
    button_close.grid(column=0, row=4)
    window.mainloop()


def calculator():
    def clicked():
        is_complete = True
        first_number = str("")
        second_number = str("")
        if expression.get().find("+") != -1:
            sign_id = expression.get().find("+")
            sign = "+"
        elif expression.get().find("-") != -1:
            sign_id = expression.get().find("-")
            sign = "-"
        elif expression.get().find("*") != -1:
            sign_id = expression.get().find("*")
            sign = "*"
        elif expression.get().find(":") != -1:
            sign_id = expression.get().find(":")
            sign = ":"
        else:
            error_window = Tk()
            is_complete = False
            error_window.title("Ошибка!")
            error_window.geometry('272x150')
            warning = Label(error_window, text="Проверьте правильность введенных данных!", bg=data["background_text"], fg=data["foreground_text"])
            warning.grid(column=0, row=0)
            error_window.mainloop()
        # First number (before sign) getting.
        for i in range(0, sign_id):
            first_number += expression.get()[i]
        # Second number (after sign) getting.
        for i in range(sign_id + 1, len(expression.get())):
            second_number += expression.get()[i]
        if sign == "+":
            answer = str(first_number) + "+" + str(second_number) + "=" + str(float(first_number) + float(second_number))
        elif sign == "-":
            answer = str(first_number) + "-" + str(second_number) + "=" + str(float(first_number) - float(second_number))
        elif sign == "*":
            answer = str(first_number) + "*" + str(second_number) + "=" + str(float(first_number) * float(second_number))
        elif sign == ":":
            if second_number == 0:
                error_window = Tk()
                error_window.title("Ошибка!")
                is_complete = False
                error_window.geometry('272x150')
                warning = Label(error_window, text="Проверьте правильность введенных данных!", bg=data["background_text"], fg=data["foreground_text"])
                warning.grid(column=0, row=0)
                error_window.mainloop()
            else:
                answer = str(first_number) + ":" + str(second_number) + "=" + str(float(first_number) / float(second_number))
        if is_complete is True:
            final_window = Tk()
            final_window.title("Результат")
            final_window.geometry('272x150')
            text = "Ответ: " + str(answer)
            main_text = Label(final_window, text=text, bg=data["background_text"], fg=data["foreground_text"])
            main_text.grid(column=0, row=0)
            final_window.mainloop()

    def closed():
        activity["details"] = "В главном меню"
        root.destroy()

    data = config_load()
    activity["details"] = "Использует калькулятор"
    root = Tk()
    root.resizable(width=False, height=False)
    root.title("MathHelper - Калькулятор")
    main_text = "Для расчетов необходимо использовать следующие знаки:\n+ - сложение\n- - вычитание\n: - деление\n* - умножение\nВводите выражение с одним знаком действия БЕЗ пробелов. Пример: 2:2; 2+3"
    l = Label(root, text=main_text, bg=data["background_text"], fg=data["foreground_text"])
    l.grid(column=0, row=0)
    expression = Entry(root, width=20, bg=data["background_entry"])
    expression.grid(column=0, row=1)
    button = Button(root, text="Ок!", command=clicked, bg=data["background_button"], fg=data["foreground_button"])
    button.grid(column=0, row=2)
    button_close = Button(root, text="Закрыть", command=closed, bg=data["background_button"],
                          fg=data["foreground_button"])
    button_close.grid(column=0, row=3)
    root.mainloop()


def picks_theorem():
    activity["details"] = "Рассчитывает площадь по теореме Пика"
    data = config_load()

    def clicked():
        if external.get().isdigit() and internal.get().isdigit():
            result = Tk()
            result.title("Результат")
            result.geometry('250x150')
            area = float(int(internal.get()) + int(external.get()) / 2 - 1)
            final_text = "Площадь равна " + str(area) + "ед."
            text = Label(result, text=final_text, bg=data["background_text"], fg=data["foreground_text"])
            text.grid(column=0, row=0)
            result.mainloop()
        else:
            error = Tk()
            error.title("Ошибка")
            error.geometry('272x150')
            txt = Label(error, text="Введите корректные данные!", bg=data["background_text"], fg=data["foreground_text"])
            txt.grid(column=0, row=0)
            error.mainloop()

    def close():
        activity["details"] = "В главном меню"
        window.destroy()
    window = Tk()
    window["bg"] = data["background"]
    window.resizable(width=False, height=False)
    window.title("MathHelper - Теорема Пика")
    window.geometry('535x180')
    main_text = Label(window, text="Для корректной работы программы введите целые и неотрицательные числа!", bg=data["background_text"], fg=data["foreground_text"])
    main_text.grid(column=0, row=0)
    external_text = Label(window, text="Количество внешних узлов", bg=data["background_text"], fg=data["foreground_text"])
    external_text.grid(column=0, row=1)
    external = Entry(window, width=10, bg=data["background_entry"])
    external.grid(column=0, row=2)
    internal_text = Label(window, text="Количество внутренних узлов", bg=data["background_text"], fg=data["foreground_text"])
    internal_text.grid(column=0, row=3)
    internal = Entry(window, width=10, bg=data["background_entry"])
    internal.grid(column=0, row=4)
    button = Button(window, text="Ок!", command=clicked, bg=data["background_button"], fg=data["foreground_button"])
    button.grid(column=0, row=5)
    button_close = Button(window, text="Закрыть", command=close, bg=data["background_button"], fg=data["foreground_button"])
    button_close.grid(column=0, row=6)
    window.mainloop()


def factorial():
    activity["details"] = "Рассчитывает факториал"
    data = config_load()

    def factorial_clicked():
        answer = 1
        try:
            int(number.get())
        except ValueError:
            error_window = Tk()
            error_window["bg"] = data["background"]
            error_window.title("Ошибка!")
            error_window.geometry('400x250')
            error = Label(error_window, text="Введите корректные данные!",
                          bg=data["background_text"], fg=data["foreground_text"])
            error.grid(column=0, row=0)
            error_window.mainloop()
        else:
            if int(number.get()) > 50000:
                error_window = Tk()
                error_window.title("Ошибка")
                error_window.geometry('530x180')
                txt = Label(error_window, text="Введите число, меньшее 50000!", bg=data["background_text"], fg=data["foreground_text"])
                txt.grid(column=0, row=0)
                error_window.mainloop()
            elif int(number.get()) <= 0:
                error_window = Tk()
                error_window.title("Ошибка")
                error_window.geometry('530x180')
                txt = Label(error_window, text="Введите число, большее 0!", bg=data["background_text"], fg=data["foreground_text"])
                txt.grid(column=0, row=0)
                error_window.mainloop()
            else:
                for i in range(1, int(number.get()) + 1):
                    answer = answer * i
                result = Tk()
                result.title("Результат")
                result.geometry('250x150')
                final_text = "Факториал числа " + str(number.get()) + " равен " + str(answer)
                main_text = Label(result, text=final_text, bg=data["background_text"], fg=data["foreground_text"])
                main_text.grid(column=0, row=0)
                result.mainloop()

    def clicked():
        activity["details"] = "В главном меню"
        window.destroy()
    window = Tk()
    window["bg"] = data["background"]
    window.resizable(width=False, height=False)
    window.title("MathHelper - Факториал")
    window.geometry('530x180')
    txt = Label(window, text="Для корректной работы программы введите целое и неотрицательное число.", bg=data["background_text"], fg=data["foreground_text"])
    txt.grid(column=0, row=0)
    text = Label(window, text="Введите целое число", bg=data["background_text"], fg=data["foreground_text"])
    text.grid(column=0, row=1)
    number = Entry(window, width=10, bg=data["background_entry"])
    number.grid(column=0, row=2)
    button = Button(window, text="Ок!", command=factorial_clicked, bg=data["background_button"], fg=data["foreground_button"])
    button.grid(column=0, row=3)
    button_close = Button(window, text="Закрыть", command=clicked, bg=data["background_button"], fg=data["foreground_button"])
    button_close.grid(column=0, row=4)
    window.mainloop()


def about():
    activity["details"] = "В панели информации о программе"
    data = config_load()

    def clicked():
        activity["details"] = "В главном меню"
        root.destroy()
    root = Tk()
    root["bg"] = data["background"]
    root.resizable(width=False, height=False)
    main_text = "Версия: v1.0\nРазработчик: DiOnFire\nИсходный код: github.com/DiOnFire/MathHelper\nНашли баг? https://github.com/DiOnFire/MathHelper/issues\n  "
    root.title("MathHelper - Информация")
    title = Label(root, text="MathHelper", font=("Arial Black", 70), bg=data["background_text"], fg=data["foreground_text"])
    title.grid(column=0, row=0)
    information = Label(root, text=main_text, bg=data["background_text"], fg=data["foreground_text"])
    information.grid(column=0, row=1)
    button = Button(root, text="Закрыть", command=clicked, bg=data["background_button"], fg=data["foreground_button"])
    button.grid(column=0, row=2)
    root.mainloop()


def settings():
    data = config_load()
    activity["details"] = "В меню настроек"

    def save():
        if is_correct_hex(background.get()) == 1:
            config["background"] = background.get()
        if is_correct_hex(background_text_entry.get()) == 1:
            config["background_text"] = background_text_entry.get()
        if is_correct_hex(foreground_text.get()) == 1:
            config["foreground_text"] = foreground_text.get()
        if is_correct_hex(foreground_button.get()) == 1:
            config["foreground_button"] = foreground_button.get()
        if is_correct_hex(background_button.get()) == 1:
            config["background_button"] = background_button.get()
        if is_correct_hex(background_entry.get()) == 1:
            config["background_entry"] = background_entry.get()
        with open("config.json", "w") as file:
            json.dump(config, file)
        root.destroy()

    def return_defaults():
        with open("config.json", "w") as file:
            json.dump(default_config, file)
        root.destroy()

    def closed():
        activity["details"] = "В главном меню"
        root.destroy()
    root = Tk()
    root["bg"] = data["background"]
    root.title("MathHelper - Настройки")
    root.geometry('279x410')
    root.resizable(width=False, height=False)
    info = Label(root, text="Введите HEX-код цвета:", bg=data["background_text"], fg=data["foreground_text"])
    info.grid(column=0, row=0)
    background_text = Label(root, text="Пользовательский цвет Background", bg=data["background_text"], fg=data["foreground_text"])
    background_text.grid(column=0, row=1)
    background = Entry(root, width=10, bg=data["background_entry"])
    background.grid(column=0, row=2)
    background_text_text = Label(root, text="Пользовательский цвет Text Background", bg=data["background_text"], fg=data["foreground_text"])
    background_text_text.grid(column=0, row=3)
    background_text_entry = Entry(root, width=10, bg=data["background_entry"])
    background_text_entry.grid(column=0, row=4)
    foreground_text_text = Label(root, text="Пользовательский цвет Text Foreground", bg=data["background_text"], fg=data["foreground_text"])
    foreground_text_text.grid(column=0, row=5)
    foreground_text = Entry(root, width=10, bg=data["background_entry"])
    foreground_text.grid(column=0, row=6)
    background_button_text = Label(root, text="Пользовательский цвет Button Background", bg=data["background_text"], fg=data["foreground_text"])
    background_button_text.grid(column=0, row=7)
    background_button = Entry(root, width=10, bg=data["background_entry"])
    background_button.grid(column=0, row=8)
    foreground_button_text = Label(root, text="Пользовательский цвет Button Foreground", bg=data["background_text"], fg=data["foreground_text"])
    foreground_button_text.grid(column=0, row=9)
    foreground_button = Entry(root, width=10, bg=data["background_entry"])
    foreground_button.grid(column=0, row=10)
    background_entry_text = Label(root, text="Пользовательский цвет Entry Background", bg=data["background_text"], fg=data["foreground_text"])
    background_entry_text.grid(column=0, row=11)
    background_entry = Entry(root, width=10, bg=data["background_entry"])
    background_entry.grid(column=0, row=12)
    button = Button(root, text="Сохранить", command=save, bg=data["background_button"], fg=data["foreground_button"])
    button.grid(column=0, row=13)
    default_button = Button(root, text="Сбросить настройки", command=return_defaults, bg=data["background_button"], fg=data["foreground_button"])
    default_button.grid(column=0, row=14)
    exit_button = Button(root, text="Выйти", command=closed, bg=data["background_button"], fg=data["foreground_button"])
    exit_button.grid(column=0, row=15)
    root.mainloop()


def menu():
    # Создаем окно
    data = config_load()
    root = Tk()
    root["bg"] = data["background"]
    root.resizable(width=False, height=False)
    root.title("MathHelper")
    root.geometry('518x640')
    # Title text
    title_text = Label(root, text="MathHelper", font=("Arial Bold", 50), bg=data["background_text"], fg=data["foreground_text"])
    title_text.place(x=120, y=1)
    # Buttons
    # Perimeter
    perimeter_button = Button(root, text="Расчет периметра", command=Perimetr, width=20, bg=data["background_button"], fg=data["foreground_button"])
    perimeter_button.place(x=45, y=64)
    # Area
    area_button = Button(root, text="Расчет площади", command=Ploshad, width=20, bg=data["background_button"], fg=data["foreground_button"])
    area_button.place(x=276, y=64)
    # Void
    void_button = Button(root, text="Расчет объема", command=Obyem, width=20, bg=data["background_button"], fg=data["foreground_button"])
    void_button.place(x=45, y=114)
    # Converter
    converter_button = Button(root, text="Конвертер величин", command=Konverter_velichin, width=20, bg=data["background_button"], fg=data["foreground_button"])
    converter_button.place(x=276, y=114)
    # Number of digits (aka nod)
    nod_button = Button(root, text="Количество цифр в числе", command=number_of_digits, width=20, bg=data["background_button"], fg=data["foreground_button"])
    nod_button.place(x=276, y=164)
    # Dividers
    dividers_button = Button(root, text="Делители числа", command=get_dividers, width=20, bg=data["background_button"], fg=data["foreground_button"])
    dividers_button.place(x=45, y=214)
    # Is simple number
    simple_button = Button(root, text="Простое число", command=simple_number, width=20, bg=data["background_button"], fg=data["foreground_button"])
    simple_button.place(x=276, y=214)
    # Calculator
    calculator_button = Button(root, text="Калькулятор", command=calculator, width=20, bg=data["background_button"], fg=data["foreground_button"])
    calculator_button.place(x=45, y=264)
    # Picks theorem
    picks_button = Button(root, text="Теорема Пика", command=picks_theorem, width=20, bg=data["background_button"], fg=data["foreground_button"])
    picks_button.place(x=276, y=264)
    # Factorial
    factorial_button = Button(root, text="Факториал", command=factorial, width=20, bg=data["background_button"], fg=data["foreground_button"])
    factorial_button.place(x=45, y=164)
    # About
    about_button = Button(root, text="О программе", command=about, width=20, bg=data["background_button"], fg=data["foreground_button"])
    about_button.place(x=169, y=560)
    # quit
    quit_button = Button(root, text="Выйти", command=close, width=20, bg=data["background_button"], fg=data["foreground_button"])
    quit_button.place(x=169, y=590)
    # settings
    settings_button = Button(root, text="Настройки", command=settings, width=20, bg=data["background_button"], fg=data["foreground_button"])
    settings_button.place(x=169, y=530)
    root.mainloop()


thread1 = threading.Thread(target=discord_rpc, daemon=True)
thread1.start()
menu()