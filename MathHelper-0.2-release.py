# Дорогой программист:
# Когда я писал этот код, только
# я и бог знали, как он работает.
# Теперь знает только бог!
# Семёнов, если ты это читаешь, то знай, ты - козёл.
# Если ты попытаешься что-нибудь
# здесь оптимизировать и у тебя
# не получится (скорее всего),
# то увеличь значение счётчика,
# как предупреждение для следующего
# человека:

# kolichestvo_chasov_potrachennih_zdec' = 3

# Variables

metr = "м"
kilometr = "км"
mm = "мм"
dc = "дм"
kg = "кг"
centneri = "ц"
gramm = "г"
tonna = "т"

# Perimeter function

def Perimetr():
    print("ВНИМАНИЕ! Если вам нужно ввести десятичную дробь, ")
    print("то используйте ТОЧКУ для разделения целой и десятичной части!")
    print()
    shirina = float(input("Введите ширину(см): ")) # Getting a
    dlina = float(input("Введите длину(см): ")) # Getting b
    if shirina > dlina: # If contradiction
        print("Ошибка: ширина не может быть больше длины! Попробуйте повторить попытку.")
    elif shirina < dlina or shirina == dlina: # Getting perimeter
        rezyltat_perimetr = dlina + shirina + dlina + shirina
        print("Ответ: ", rezyltat_perimetr, " сантиметров.")

# Area function

def Ploshad():
    print("ВНИМАНИЕ! Если вам нужно ввести десятичную дробь,")
    print("то используйте ТОЧКУ для разделения целой и десятичной части!")
    print()
    shirina = float(input("Введите ширину(см): ")) # Getting a
    dlina = float(input("Введите длину(см): ")) # Getting b
    if shirina > dlina: # If contradiction
        print("Ошибка: ширина не может быть больше длины! Попробуйте повторить попытку.")
    elif shirina < dlina or shirina == dlina: # Getting area
        rezyltat_ploshad = dlina * shirina
        print("Ответ: ", rezyltat_ploshad, " сантиметров в квадрате.")


def Obyem():
    print("ВНИМАНИЕ! Если вам нужно ввести десятичную дробь, ")
    print("то используйте ТОЧКУ для разделения целой и десятичной части!")
    print()
    shirina = float(input("Введите ширину(см): "))
    dlina = float(input("Введите длину(см): "))
    visota = float(input("Введите высоту(см): "))
    if shirina > dlina:
        print("Ошибка: ширина не может быть больше длины! Попробуйте повторить попытку.")
    elif shirina < dlina or shirina == dlina:
        rezyltat_obyem = dlina * shirina * visota
        print("Ответ: ", rezyltat_obyem, " сантиметров в кубе.")


def Konverter_velichin():
    print("ВНИМАНИЕ! Если вам нужно ввести десятичную дробь, ")
    print("то используйте ТОЧКУ для разделения целой и десятичной части!")
    print()
    print("ВНИМАНИЕ! При вводе типа величины используйте сокращения, как показано в скобках!")
    print()
    znachenie_velichini = float(input("Введите значение величины: "))
    print()
    print("1 - Миллиметры")
    print("2 - Сантиметры")
    print("3 - Дециметры")
    print("4 - Метры")
    print("5 - Километры")
    print("6 - Граммы")
    print("7 - Килограммы")
    print("8 - Цейнтнеры")
    print("9 - Тонны")
    tip_velichini = str(input("Введите тип величины (Введите номер нужного пункта): "))
    print()
    print("1 - Миллиметры")
    print("2 - Сантиметры")
    print("3 - Дециметры")
    print("4 - Метры")
    print("5 - Километры")
    print("6 - Граммы")
    print("7 - Килограммы")
    print("8 - Цейнтнеры")
    print("9 - Тонны")
    konechnii_tip_velichini = str(input("В какую величину вы хотите перевести(Введите номер нужного пункта): "))
    if tip_velichini == "2" and konechnii_tip_velichini == "2":
        print()
        print("Ответ: ", znachenie_velichini)
    elif tip_velichini == "4" and konechnii_tip_velichini == "2":
        answer = znachenie_velichini * 100
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "1" and konechnii_tip_velichini == "2":
        answer = znachenie_velichini / 10
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "5" and konechnii_tip_velichini == "2":
        answer = znachenie_velichini * 1000000
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "3" and konechnii_tip_velichini == "2":
        answer = znachenie_velichini * 10
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "2" and konechnii_tip_velichini == "1":
        answer = znachenie_velichini * 10
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "4" and konechnii_tip_velichini == "1":
        answer = znachenie_velichini * 1000
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "1" and konechnii_tip_velichini == "1":
        print()
        print("Ответ: ", znachenie_velichini)
    elif tip_velichini == "5" and konechnii_tip_velichini == "1":
        answer = znachenie_velichini * 10000000
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "3" and konechnii_tip_velichini == "1":
        answer = znachenie_velichini * 100
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "2" and konechnii_tip_velichini == "4":
        answer = znachenie_velichini / 100
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "4" and konechnii_tip_velichini == "4":
        print()
        print("Ответ: ", znachenie_velichini)
    elif tip_velichini == "1" and konechnii_tip_velichini == "4":
        answer = znachenie_velichini / 1000
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "5" and konechnii_tip_velichini == "4":
        answer = znachenie_velichini / 1000
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "3" and konechnii_tip_velichini == "4":
        answer = znachenie_velichini / 10
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "2" and konechnii_tip_velichini == "3":
        answer = znachenie_velichini / 10
        print()
        print("Ответ: ", znachenie_velichini)
    elif tip_velichini == "4" and konechnii_tip_velichini == "3":
        answer = znachenie_velichini / 10
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "1" and konechnii_tip_velichini == "3":
        answer = znachenie_velichini / 10
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "5" and konechnii_tip_velichini == "3":
        answer = znachenie_velichini / 10
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "3" and konechnii_tip_velichini == "3":
        print()
        print("Ответ: ", znachenie_velichini)
    elif tip_velichini == "2" and konechnii_tip_velichini == "5":  # kilometri
        answer = znachenie_velichini / 1000000
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "4" and konechnii_tip_velichini == "5":
        answer = znachenie_velichini / 1000
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "1" and konechnii_tip_velichini == "5":
        answer = znachenie_velichini / 10000000
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "5" and konechnii_tip_velichini == "5":
        print()
        print("Ответ: ", znachenie_velichini)
    elif tip_velichini == "3" and konechnii_tip_velichini == "5":
        answer = znachenie_velichini / 100
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "6" and konechnii_tip_velichini == "6":
        print()
        print("Ответ: ", znachenie_velichini)
    elif tip_velichini == "6" and konechnii_tip_velichini == "7":
        answer = znachenie_velichini / 1000
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "6" and konechnii_tip_velichini == "8":
        answer = znachenie_velichini / 100000
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "6" and konechnii_tip_velichini == "9":
        answer = znachenie_velichini / 1000000
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "7" and konechnii_tip_velichini == "6":
        answer = znachenie_velichini * 1000
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "7" and konechnii_tip_velichini == "7":
        print()
        print("Ответ: ", znachenie_velichini)
    elif tip_velichini == "7" and konechnii_tip_velichini == "8":
        answer = znachenie_velichini / 100
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "7" and konechnii_tip_velichini == "9":
        answer = znachenie_velichini / 1000
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "8" and konechnii_tip_velichini == "6":
        answer = znachenie_velichini * 100000
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "8" and konechnii_tip_velichini == "7":
        answer = znachenie_velichini * 100
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "8" and konechnii_tip_velichini == "8":
        print()
        print("Ответ: ", znachenie_velichini)
    elif tip_velichini == "8" and konechnii_tip_velichini == "9":
        answer = znachenie_velichini / 10
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "9" and konechnii_tip_velichini == "6":
        answer = znachenie_velichini * 1000000
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "9" and konechnii_tip_velichini == "7":
        answer = znachenie_velichini * 1000
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "9" and konechnii_tip_velichini == "8":
        answer = znachenie_velichini * 10
        print()
        print("Ответ: ", answer)
    elif tip_velichini == "9" and konechnii_tip_velichini == "9":
        print()
        print("Ответ: ", znachenie_velichini)
    else:
        print()
        print("Ошибка конвертации! Попробуйте повторить попытку.")


def Reshatel_yravnenii():
    print()
    print("1 - умножение")
    print("2 - деление")
    print("3 - сложение")
    print("4 - вычитание")
    print("Какое действие является основным в уравнении: ")
    deistvie_yravnenie = str(input())
    print()
    if deistvie_yravnenie == "1":
        znak = "×"
        print()
        first_mnojitel = str(
            input("Введите значение первого множителя (если является корнем уравнения, то введите '!'): "))
        if first_mnojitel == "!":
            first_mnojitel = str(first_mnojitel)
        else:
            first_mnojitel = float(first_mnojitel)
        print()
        second_mnojitel = str(input("Введите значение второго множителя (если является корнем уравнения, то введите !): "))
        if second_mnojitel == "!":
            second_mnojitel = str(second_mnojitel)
        else:
            second_mnojitel = float(second_mnojitel)
        print()
        print("Введите значение произведения: ")
        proizvedenie = float(input())
        if first_mnojitel == "!":
            answer = proizvedenie / second_mnojitel
            print()
            print("X", znak, second_mnojitel, "=", proizvedenie)
            print("X", "=", proizvedenie, ":", second_mnojitel)
            print("X", "=", answer)
            print("Ответ: ", answer)
        elif second_mnojitel == "!":
            answer = proizvedenie / first_mnojitel
            print()
            print(first_mnojitel, znak, "X", "=", proizvedenie)
            print("X", "=", proizvedenie, ":", first_mnojitel)
            print("X", "=", answer)
            print("Ответ: ", answer)
    elif deistvie_yravnenie == "3":
        znak = "+"
        print()
        print("Введите значение первого слагаемого (если является корнем уравнения, то введите !): ")
        first_slagaemoe = str(input())
        if first_slagaemoe == "!":
            first_slagaemoe = str(first_slagaemoe)
        else:
            first_slagaemoe = float(first_slagaemoe)
        print()
        print("Введите значение второго слагаемого (если является корнем уравнения, то введите !): ")
        second_slagaemoe = str(input())
        if second_slagaemoe == "!":
            second_slagaemoe = str(second_slagaemoe)
        else:
            second_slagaemoe = float(second_slagaemoe)
        print()
        print("Введите значение суммы: ")
        symma_yravnenie = float(input())
        if first_slagaemoe == "!":
            print()
            answer = symma_yravnenie - second_slagaemoe
            print()
            print(first_slagaemoe, znak, second_slagaemoe, "=", symma_yravnenie)
            print(first_slagaemoe, "=", symma_yravnenie, "-", second_slagaemoe)
            print(first_slagaemoe, "=", answer)
            print("Ответ: ", answer)
        elif second_slagaemoe == "!":
            print()
            answer = symma_yravnenie - first_slagaemoe
            print()
            print(first_slagaemoe, znak, second_slagaemoe, "=", symma_yravnenie)
            print(second_slagaemoe, "=", symma_yravnenie, "-", first_slagaemoe)
            print("Ответ: ", answer)
    elif deistvie_yravnenie == "2":
        znak = ":"
        print()
        print("Введите значение делимого (если является корнем уравнения, то введите !): ")
        delimoe_yravnenie = str(input())
        if delimoe_yravnenie == "!":
            delimoe_yravnenie = str(delimoe_yravnenie)
        else:
            delimoe_yravnenie = float(delimoe_yravnenie)
        print()
        print("Введите значение делителя (если является корнем уравнения, то введите !): ")
        delitel_yravnenie = str(input())
        if delitel_yravnenie == "!":
            delitel_yravnenie == str(delitel_yravnenie)
        else:
            delitel_yravnenie == float(delitel_yravnenie)
            print()
            print("Введите значение частного: ")
            chastnoe_yravnenie = str(input())
            if delimoe_yravnenie == "!":
                print()
                answer = chastnoe_yravnenie / delitel_yravnenie
                print(delimoe_yravnenie, znak, delitel_yravnenie, "=", chastnoe_yravnenie)
                print(delimoe_yravnenie, "=", chastnoe_yravnenie, znak, delitel_yravnenie)
                print("Ответ: ", answer)
            elif delitel_yravnenie == "!":
                answer = chastnoe_yravnenie / delimoe_yravnenie
                print()
                print(delimoe_yravnenie, znak, delitel_yravnenie, "=", chastnoe_yravnenie)
                print(delitel_yravnenie, "=", chastnoe_yravnenie, znak, delimoe_yravnenie)
                print("Ответ: ", answer)
    elif deistvie_yravnenie == "4":
        znak = "-"
        print()
        print("Введите значение уменьшаемого (если является корнем уравнения, то введите !): ")
        ymenshaemoe_yravnenie = str(input())
        if ymenshaemoe_yravnenie == "!":
            ymenshaemoe_yravnenie = str(ymenshaemoe_yravnenie)
        else:
            ymenshaemoe_yravnenie = float(ymenshaemoe_yravnenie)
        print()
        print("Введите значение вычитаемого (если является корнем уравнения, то введите !): ")
        vichitaemoe_yravnenie = str(input())
        if vichitaemoe_yravnenie == "!":
            vichitaemoe_yravnenie = str(vichitaemoe_yravnenie)
        else:
            vichitaemoe_yravnenie = float(vichitaemoe_yravnenie)
        print()
        print("Введите значение разности: ")
        raznost_yravnenie = str(input())
        print()
        if ymenshaemoe_yravnenie == "!":
            answer = vichitaemoe_yravnenie + raznost_yravnenie
            print()
            print(ymenshaemoe_yravnenie, znak, vichitaemoe_yravnenie, "=", raznost_yravnenie)
            print(ymenshaemoe_yravnenie, "=", raznost_yravnenie, "+", vichitaemoe_yravnenie)
            print(ymenshaemoe_yravnenie, "=", answer)
            print("Ответ: ", answer)
        elif vichitaemoe_yravnenie == "!":
            answer = ymenshaemoe_yravnenie - raznost_yravnenie
            print()
            print(ymenshaemoe_yravnenie, znak, vichitaemoe_yravnenie, "=", raznost_yravnenie)
            print(vichitaemoe_yravnenie, "=", ymenshaemoe_yravnenie, znak, raznost_yravnenie)
            print(vichitaemoe_yravnenie, "=", answer)
            print("Ответ: ", answer)


def number_of_digits():
    print()
    number = str(input("Введите целое число: "))
    counter = len(number)
    print("Вы ввели ", counter, "- значное число.")


def get_dividers():
    print()
    number = int(input("Введите целое число: "))
    for i in range(1, number + 1):
        if number % i == 0:
            print(i, end="; ")


def simple_number():
    print()
    is_simple = True
    number = int(input("Введите целое число: "))
    for i in range(2, number):
        if number % i == 0:
            is_simple = False
    if is_simple is True:
        print("Введённое число - простое.")
    elif is_simple is False:
        print("Введённое число не является простым.")


def calculator():
    print()
    first_number = str("")
    second_number = str("")
    print("Для расчетов необходимо использовать следующие знаки:")
    print("+ - сложение.")
    print("- - вычитание.")
    print(": - деление.")
    print("* - умножение.")
    print("Вводите выражение с одним знаком действия БЕЗ пробелов. Пример: 2:2; 2+3.")
    expression = str(input())
    if expression.find("+") != -1:
        sign_id = expression.find("+")
        sign = "+"
    elif expression.find("-") != -1:
        sign_id = expression.find("-")
        sign = "-"
    elif expression.find("*") != -1:
        sign_id = expression.find("*")
        sign = "*"
    elif expression.find(":") != -1:
        sign_id = expression.find(":")
        sign = ":"
    else:
        print("ОШИБКА: Знак операции не найден.")
        return 0
    # First number (before sign) getting.
    for i in range(0, sign_id):
        first_number += expression[i]
    # Second number (after sign) getting.
    for i in range(sign_id + 1, len(expression)):
        second_number += expression[i]
    if sign == "+":
        print(first_number, "+", second_number, "=", float(first_number) + float(second_number))
    elif sign == "-":
        print(first_number, "-", second_number, "=", float(first_number) - float(second_number))
    elif sign == "*":
        print(first_number, "*", second_number, "=", float(first_number) * float(second_number))
    elif sign == ":":
        if second_number == 0:
            print("ОШИБКА: Делить на 0 нельзя!")
            return 0
        else:
            print(first_number, ":", second_number, "=", float(first_number) / float(second_number))


def picks_theorem():
    print()
    external = int(input("Введите количество внешних узлов фигуры: ")) # "n" in formula
    internal = int(input("Введите количество внутренних узлов фигуры: ")) # "m" in formula
    area = float(internal + external / 2 - 1)
    print()
    print("Площадь фигуры по теореме Пика равна", area, "ед.")


def factorial():
    print()
    answer = 1
    number = int(input("Введите целое число: "))
    if number > 0:
        for i in range(1, number + 1):
            answer = answer * i
    else:
        print("ОШИБКА: Введите число, большее, чем 0!")
        return 0
    print()
    print("Факториал числа", number, "равен", answer)


def middle_value():
    print()
    summ = 0
    values_number = int(input("Введите количество значений, с которыми необходимо произвести расчёты: "))
    for i in range(values_number):
        data = int(input("Введите значение #", i, ":", sep=""))
        summ += data
    print("Среднее арифметическое: ", summ / values_number)


def about():
    print()
    print("-=-=-=-= MathsHelper =-=-=-=-")
    print()
    print("Вы используете версию: v0.2-release")
    print("Разработчик: Максим Батарон.")
    print("Связаться с разработчиком: di0nik.gd@gmail.com")
    print("YouTube-канал разработчика: https://www.youtube.com/c/DiOnFire")
    print()
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print()
    print("Программа имеет открытый исходный код, просмотреть его можно здесь:")
    print("Репозиторий на GitHub: https://github.com/DiOnFire/MathHelper")


def manager(function):
    if function == "1":
        Perimetr()
    elif function == "2":
        Ploshad()
    elif function == "3":
        Obyem()
    elif function == "4":
        Konverter_velichin()
    elif function == "5":
        Reshatel_yravnenii()
    elif function == "6":
        number_of_digits()
    elif function == "7":
        get_dividers()
    elif function == "8":
        simple_number()
    elif function == "9":
        calculator()
    elif function == "10":
        picks_theorem()
    elif function == "11":
        factorial()
    elif function == "12":
        middle_value()
    elif function == "A" or function == "a":
        about()
    else:
        exit()


print()
print("======================================================")
print("Добро пожаловать в MathsHelper!")
print("Эта программа поможет вам с математическими расчетами!")
print("Введите цифру интересующей вас функции.")
print("======================================================")
while True:
    print()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("1 - Вычислить периметр.")
    print("2 - Вычислить площадь.")
    print("3 - Вычислить объём.")
    print("4 - Конвертер величин.")
    print("5 - Решить уравнение (простое).")
    print("6 - Вычислить количество цифр в числе.")
    print("7 - Просмотреть все делители числа.")
    print("8 - Проверить, является ли число простым.")
    print("9 - Калькулятор.")
    print("10 - Расчёт площади фигуры по теореме Пика.")
    print("11 - Расчёт факториала числа.")
    print("12 - Расчёт среднего арифметического значения.")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("A - Просмотр информации о программе.")
    print("Для выхода введите любой другой символ.")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print()
    Function = str(input("Номер функции: "))
    manager(Function)