# Дорогой программист:
# Когда я писал этот код, только
# я и бог знали, как он работает.
# Теперь знает только бог!
#
# Если ты попытаешься что-нибудь
# здесь оптимизировать и у тебя
# не получится (скорее всего),
# то увеличь значение счётчика,
# как предупреждение для следующего
# человека:
#
# kolichestvo_chasov_potrachennih_zdec' = 1

#Peremennie

metr = "м"

kilometr = "км"
mm = "мм"
dc = "дм"
kg = "кг"
centneri = "ц"
gramm = "г"
tonna = "т"

#Import modules

import time

#Functions

def Perimetr():

    time.sleep(0.5)
    print u"ВНИМАНИЕ! Если вам нужно ввести десятичную дробь, то используйте ТОЧКУ для разделения целой и десятичной части!"
    print
    print u"Введите ширину(см): ",
    shirina = raw_input()
    time.sleep(0.5)
    shirina = float(shirina)
    print u"Введите длину(см): ",
    dlina = raw_input()
    dlina = float(dlina)
    if shirina > dlina:

        time.sleep(0.5)
        print u"Ошибка: ширина не может быть больше длины! Попробуйте повторить попытку."

    else:

        if shirina < dlina or shirina == dlina:

            rezyltat_perimetr = dlina + shirina + dlina + shirina
            time.sleep(0.5)
            print u"Ответ: ", rezyltat_perimetr, " сантиметров."

def Ploshad():

    time.sleep(0.5)
    print u"ВНИМАНИЕ! Если вам нужно ввести десятичную дробь, то используйте ТОЧКУ для разделения целой и десятичной части!"
    print
    print u"Введите ширину(см): ",
    shirina = raw_input()
    shirina = float(shirina)
    time.sleep(0.5)
    print u"Введите длину(см): ",
    dlina = raw_input()
    dlina = float(dlina)
    if shirina > dlina:

        time.sleep(0.5)
        print u"Ошибка: ширина не может быть больше длины! Попробуйте повторить попытку."

    else:

        if shirina < dlina or shirina == dlina:

            rezyltat_ploshad = dlina * shirina
            time.sleep(0.5)
            print u"Ответ: ", rezyltat_ploshad, " сантиметров в квадрате."

def Obyem():

    time.sleep(0.5)
    print u"ВНИМАНИЕ! Если вам нужно ввести десятичную дробь, то используйте ТОЧКУ для разделения целой и десятичной части!"
    print
    print u"Введите ширину(см): ",
    shirina = raw_input()
    shirina = float(shirina)
    time.sleep(0.5)
    print u"Введите длину(см): ",
    dlina = raw_input()
    dlina = float(dlina)
    time.sleep(0.5)
    print u"Введите высоту(см): ",
    visota = raw_input()
    visota = float(visota)

    if shirina > dlina:

        time.sleep(0.5)
        print u"Ошибка: ширина не может быть больше длины! Попробуйте повторить попытку."

    else:

        if shirina < dlina or shirina == dlina:

            rezyltat_obyem = dlina * shirina * visota
            time.sleep(0.5)
            print u"Ответ: ", rezyltat_obyem, u" сантиметров в кубе."

def Konverter_velichin():

    time.sleep(0.5)
    print u"ВНИМАНИЕ! Если вам нужно ввести десятичную дробь, то используйте ТОЧКУ для разделения целой и десятичной части!"
    print
    print u"ВНИМАНИЕ! При вводе типа величины используйте сокращения, как показано в скобках!"
    print 
    print u"Введите значение величины: ",
    znachenie_velichini = raw_input()
    znachenie_velichini = float(znachenie_velichini)
    print
    print "1 - Миллиметры"
    print "2 - Сантиметры"
    print "3 - Дециметры"
    print "4 - Метры"
    print "5 - Километры"
    print "6 - Граммы"
    print "7 - Килограммы"
    print "8 - Цейнтнеры"
    print "9 - Тонны"
    print u"Введите тип величины(Введите номер нужного пункта): ",
    tip_velichini = raw_input().encode('utf8')
    tip_velichini = str(tip_velichini)
    print
    print "1 - Миллиметры"
    print "2 - Сантиметры"
    print "3 - Дециметры"
    print "4 - Метры"
    print "5 - Километры"
    print "6 - Граммы"
    print "7 - Килограммы"
    print "8 - Цейнтнеры"
    print "9 - Тонны"
    print u"В какую величину вы хотите перевести(Введите номер нужного пункта): ",
    konechnii_tip_velichini = raw_input().encode('utf8')
    konechnii_tip_velichini = str(konechnii_tip_velichini)

    if tip_velichini == "2" and konechnii_tip_velichini == "2":   #"2"
        print 
        print u"Ответ: ", znachenie_velichini 

    else:

        if tip_velichini == "4" and konechnii_tip_velichini == "2":

            otvet = znachenie_velichini * 100
            print
            print u"Ответ: ", otvet, 

        else:

            if tip_velichini == "1" and konechnii_tip_velichini == "2":

                otvet = znachenie_velichini / 10
                print
                print u"Ответ: ", otvet, 

            else:

                if tip_velichini == "5" and konechnii_tip_velichini == "2":

                    otvet = znachenie_velichini * 1000000
                    print
                    print u"Ответ: ", otvet, 

                else:

                    if tip_velichini == "3" and konechnii_tip_velichini == "2":

                        otvet = znachenie_velichini * 10
                        print
                        print u"Ответ: ", otvet, 

                    

                    else:      #millimetr

                        if tip_velichini == "2" and konechnii_tip_velichini == "1":

                            otvet = znachenie_velichini * 10
                            print 
                            print u"Ответ: ", otvet, 

                        else:

                            if tip_velichini == "4" and konechnii_tip_velichini == "1":

                                otvet = znachenie_velichini * 1000
                                print
                                print u"Ответ: ", otvet, 

                            else:

                                if tip_velichini == "1" and konechnii_tip_velichini == "1":

                                    print
                                    print u"Ответ: ", znachenie_velichini 

                                else:

                                    if tip_velichini == "5" and konechnii_tip_velichini == "1":

                                        otvet = znachenie_velichini * 10000000
                                        print
                                        print u"Ответ: ", otvet, 

                                    else:

                                        if tip_velichini == "3" and konechnii_tip_velichini == "1":

                                            otvet = znachenie_velichini * 100
                                            print
                                            print u"Ответ: ", otvet, 

                                        else:

                                            if tip_velichini == "2" and konechnii_tip_velichini == "4":

                                                otvet = znachenie_velichini / 100
                                                print 
                                                print u"Ответ: ", otvet, 

                                            else:

                                                if tip_velichini == "4" and konechnii_tip_velichini == "4":

                                                    print
                                                    print u"Ответ: ", znachenie_velichini 

                                                else:

                                                    if tip_velichini == "1" and konechnii_tip_velichini == "4":

                                                        otvet = znachenie_velichini / 1000
                                                        print
                                                        print u"Ответ: ", otvet, 

                                                    else:

                                                        if tip_velichini == "5" and konechnii_tip_velichini == "4":

                                                            otvet = znachenie_velichini / 1000
                                                            print
                                                            print u"Ответ: ", otvet, 

                                                        else:

                                                            if tip_velichini == "3" and konechnii_tip_velichini == "4":

                                                                otvet = znachenie_velichini / 10
                                                                print
                                                                print u"Ответ: ", otvet, 

                                                            else:                                                                                        

                                                                if tip_velichini == "2" and konechnii_tip_velichini == "3":

                                                                    otvet = znachenie_velichini / 10
                                                                    print 
                                                                    print u"Ответ: ", znachenie_velichini 

                                                                else:

                                                                    if tip_velichini == "4" and konechnii_tip_velichini == "3":

                                                                        otvet = znachenie_velichini / 10
                                                                        print
                                                                        print u"Ответ: ", otvet, 

                                                                    else:

                                                                        if tip_velichini == "1" and konechnii_tip_velichini == "3":

                                                                            otvet = znachenie_velichini / 10
                                                                            print
                                                                            print u"Ответ: ", otvet, 

                                                                        else:

                                                                            if tip_velichini == "5" and konechnii_tip_velichini == "3":

                                                                                otvet = znachenie_velichini / 10
                                                                                print
                                                                                print u"Ответ: ", otvet, 

                                                                            else:

                                                                                if tip_velichini == "3" and konechnii_tip_velichini == "3":

                                                                                    print
                                                                                    print u"Ответ: ", znachenie_velichini 

                                                                                                                                

                                                                                                                                    

                                                                                else:     #kilometri

                                                                                    if tip_velichini == "2" and konechnii_tip_velichini == "5":

                                                                                        otvet = znachenie_velichini / 1000000
                                                                                        print 
                                                                                        print u"Ответ: ", otvet, 

                                                                                    else:

                                                                                        if tip_velichini == "4" and konechnii_tip_velichini == "5":

                                                                                            otvet = znachenie_velichini / 1000
                                                                                            print
                                                                                            print u"Ответ: ", otvet, 

                                                                                        else:

                                                                                            if tip_velichini == "1" and konechnii_tip_velichini == "5":

                                                                                                otvet = znachenie_velichini / 10000000
                                                                                                print
                                                                                                print u"Ответ: ", otvet, 

                                                                                            else:

                                                                                                if tip_velichini == "5" and konechnii_tip_velichini == "5":
                                                                                                                                                                    
                                                                                                    print
                                                                                                    print u"Ответ: ", znachenie_velichini 

                                                                                                else:

                                                                                                    if tip_velichini == "3" and konechnii_tip_velichini == "5":

                                                                                                        otvet = znachenie_velichini / 100
                                                                                                        print
                                                                                                        print u"Ответ: ", otvet, 

                                                                                                    else:

                                                                                                                                                                        
                                                                                                        if tip_velichini == "6" and konechnii_tip_velichini == "6":

                                                                                                            print
                                                                                                            print u"Ответ: ", znachenie_velichini 

                                                                                                        else:

                                                                                                            if tip_velichini == "6" and konechnii_tip_velichini == "7":

                                                                                                                otvet = znachenie_velichini / 1000
                                                                                                                print
                                                                                                                print u"Ответ: ", otvet, 

                                                                                                            else:

                                                                                                                if tip_velichini == "6" and konechnii_tip_velichini == "8":

                                                                                                                    otvet = znachenie_velichini / 100000
                                                                                                                    print
                                                                                                                    print u"Ответ: ", otvet, 

                                                                                                                else:

                                                                                                                    if tip_velichini == "6" and konechnii_tip_velichini == "9":

                                                                                                                        otvet = znachenie_velichini / 1000000
                                                                                                                        print
                                                                                                                        print u"Ответ: ", otvet, 

                                                                                                                    else:

                                                                                                                        if tip_velichini == "7" and konechnii_tip_velichini == "6":

                                                                                                                            otvet = znachenie_velichini * 1000
                                                                                                                            print
                                                                                                                            print u"Ответ: ", otvet, 

                                                                                                                        else:

                                                                                                                            if tip_velichini == "7" and konechnii_tip_velichini == "7":

                                                                                                                                print
                                                                                                                                print u"Ответ: ", znachenie_velichini 

                                                                                                                            else:

                                                                                                                                if tip_velichini == "7" and konechnii_tip_velichini == "8":

                                                                                                                                    otvet = znachenie_velichini / 100
                                                                                                                                    print
                                                                                                                                    print u"Ответ: ", otvet, 

                                                                                                                                else:

                                                                                                                                    if tip_velichini == "7" and konechnii_tip_velichini == "9":

                                                                                                                                        otvet = znachenie_velichini / 1000
                                                                                                                                        print
                                                                                                                                        print u"Ответ: ", otvet, 

                                                                                                                                    else:

                                                                                                                                        if tip_velichini == "8" and konechnii_tip_velichini == "6":

                                                                                                                                            otvet = znachenie_velichini * 100000
                                                                                                                                            print
                                                                                                                                            print u"Ответ: ", otvet, 

                                                                                                                                        else:

                                                                                                                                            if tip_velichini == "8" and konechnii_tip_velichini == "7":

                                                                                                                                                otvet = znachenie_velichini * 100
                                                                                                                                                print
                                                                                                                                                print u"Ответ: ", otvet, 

                                                                                                                                            else:

                                                                                                                                                if tip_velichini == "8" and konechnii_tip_velichini == "8":

                                                                                                                                                    print
                                                                                                                                                    print u"Ответ: ", znachenie_velichini 

                                                                                                                                                else:

                                                                                                                                                    if tip_velichini == "8" and konechnii_tip_velichini == "9":

                                                                                                                                                        otvet = znachenie_velichini / 10
                                                                                                                                                        print
                                                                                                                                                        print u"Ответ: ", otvet, 

                                                                                                                                                    else:

                                                                                                                                                        if tip_velichini == "9" and konechnii_tip_velichini == "6":

                                                                                                                                                            otvet = znachenie_velichini * 1000000
                                                                                                                                                            print
                                                                                                                                                            print u"Ответ: ", otvet, 

                                                                                                                                                        else:

                                                                                                                                                            if tip_velichini == "9" and konechnii_tip_velichini == "7":
                                                                                                                                                                                                                                    
                                                                                                                                                                otvet = znachenie_velichini * 1000
                                                                                                                                                                print
                                                                                                                                                                print u"Ответ: ", otvet, 

                                                                                                                                                            else:

                                                                                                                                                                if tip_velichini == "9" and konechnii_tip_velichini == "8":

                                                                                                                                                                    otvet = znachenie_velichini * 10
                                                                                                                                                                    print
                                                                                                                                                                    print u"Ответ: ", otvet, 

                                                                                                                                                                else:

                                                                                                                                                                    if tip_velichini == "9" and konechnii_tip_velichini == "9":
                                                                                                                                                                                                     
                                                                                                                                                                        print
                                                                                                                                                                        print u"Ответ: ", znachenie_velichini 

                                                                                                                                                                    else:

                                                                                                                                                                        print
                                                                                                                                                                        print "Ошибка конвертации! Попробуйте повторить попытку."                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                        
def Reshatel_yravnenii():

    time.sleep(0.5)
    print
    print u"1 - умножение"
    print u"2 - деление"
    print u"3 - сложение"
    print u"4 - вычитание"
    print u"Какое действие является основным в уравнении: ",
    deistvie_yravnenie = raw_input().encode('utf-8')
    print
    if deistvie_yravnenie == "1":

        znak = "×"
        print
        print u"Введите значение первого множителя (если является корнем уравнения, то введите !): ",
        first_mnojitel = raw_input()
        if first_mnojitel == "!":

            first_mnojitel = str(first_mnojitel)

        else:

            first_mnojitel = float(first_mnojitel)

        print
        print u"Введите значение второго множителя (если является корнем уравнения, то введите !): ",
        second_mnojitel = raw_input()
        if second_mnojitel == "!":

            second_mnojitel = str(second_mnojitel)

        else:

            second_mnojitel = float(second_mnojitel)

        print
        print u"Введите значение произведения: ",
        proizvedenie = raw_input()
        proizvedenie = float(proizvedenie)
        if first_mnojitel == "!":

            otvet = proizvedenie / second_mnojitel
            print
            print "X", znak, second_mnojitel, "=", proizvedenie
            print "X", "=", proizvedenie, ":", second_mnojitel
            print "X", "=", otvet
            print u"Ответ: ", otvet

        if second_mnojitel == "!":

            otvet = proizvedenie / first_mnojitel
            print
            print first_mnojitel, znak, "X", "=", proizvedenie
            print "X", "=", proizvedenie, ":", first_mnojitel
            print "X", "=", otvet
            print u"Ответ: ", otvet

    else:

        if deistvie_yravnenie == "3":

            znak = "+"
            print
            print u"Введите значение первого слагаемого (если является корнем уравнения, то введите !): ",
            first_slagaemoe = raw_input()
            if first_slagaemoe == "!":

                first_slagaemoe = str(first_slagaemoe)

            else:

                first_slagaemoe = float(first_slagaemoe)

            print
            print u"Введите значение второго слагаемого (если является корнем уравнения, то введите !): ",
            second_slagaemoe = raw_input()
            if second_slagaemoe == "!":

                second_slagaemoe = str(second_slagaemoe)

            else:

                second_slagaemoe = float(second_slagaemoe)

            print
            print u"Введите значение суммы: ",
            symma_yravnenie = raw_input()
            symma_yravnenie = float(symma_yravnenie)
            if first_slagaemoe == "!":

                print
                otvet = symma_yravnenie - second_slagaemoe
                print
                print first_slagaemoe, znak, second_slagaemoe, "=", symma_yravnenie
                print first_slagaemoe, "=", symma_yravnenie, "-", second_slagaemoe
                print first_slagaemoe, "=", otvet
                print u"Ответ: ", otvet

            else:

                if second_slagaemoe == "!":

                    print
                    otvet = symma_yravnenie - first_slagaemoe
                    print
                    print first_slagaemoe, znak, second_slagaemoe, "=", symma_yravnenie
                    print second_slagaemoe, "=", symma_yravnenie, "-", first_slagaemoe
                    print u"Ответ: ", otvet

        else:

            if deistvie_yravnenie == "2":

                znak = ":"
                print
                print u"Введите значение делимого (если является корнем уравнения, то введите !): ",
                delimoe_yravnenie = raw_input()
                if delimoe_yravnenie == "!":

                    delimoe_yravnenie = str(delimoe_yravnenie)

                else:

                    delimoe_yravnenie = float(delimoe_yravnenie)

                print
                print u"Введите значение делителя (если является корнем уравнения, то введите !): ",
                delitel_yravnenie = raw_input()
                if delitel_yravnenie == "!":

                    delitel_yravnenie == str(delitel_yravnenie)

                else:

                    delitel_yravnenie == float(delitel_yravnenie)

                print
                print u"Введите значение частного: ",
                chastnoe_yravnenie = raw_input()
                if delimoe_yravnenie == "!":

                    print
                    otvet = chastnoe_yravnenie / delitel_yravnenie
                    print delimoe_yravnenie, znak, delitel_yravnenie, "=", chastnoe_yravnenie
                    print delimoe_yravnenie, "=", chastnoe_yravnenie, znak, delitel_yravnenie
                    print u"Ответ: ", otvet

                else:

                    if delitel_yravnenie == "!":

                        otvet = chastnoe_yravnenie / delimoe_yravnenie
                        print
                        print delimoe_yravnenie, znak, delitel_yravnenie, "=", chastnoe_yravnenie
                        print delitel_yravnenie, "=", chastnoe_yravnenie, znak, delimoe_yravnenie
                        print u"Ответ: ", otvet

            else:

                if deistvie_yravnenie == "4":

                    znak = "-"
                    print
                    print u"Введите значение уменьшаемого (если является корнем уравнения, то введите !): ",
                    ymenshaemoe_yravnenie = raw_input()
                    if ymenshaemoe_yravnenie == "!":

                        ymenshaemoe_yravnenie = str(ymenshaemoe_yravnenie)

                    else:

                        ymenshaemoe_yravnenie = float(ymenshaemoe_yravnenie)

                    print
                    print u"Введите значение вычитаемого (если является корнем уравнения, то введите !): ",
                    vichitaemoe_yravnenie = raw_input()
                    if vichitaemoe_yravnenie == "!":

                        vichitaemoe_yravnenie = str(vichitaemoe_yravnenie)

                    else:

                        vichitaemoe_yravnenie = float(vichitaemoe_yravnenie)

                    print
                    print u"Введите значение разности: ",
                    raznost_yravnenie = raw_input()
                    print
                    if ymenshaemoe_yravnenie == "!":

                        otvet = vichitaemoe_yravnenie + raznost_yravnenie
                        print
                        print ymenshaemoe_yravnenie, znak, vichitaemoe_yravnenie, "=", raznost_yravnenie
                        print ymenshaemoe_yravnenie, "=", raznost_yravnenie, "+", vichitaemoe_yravnenie
                        print ymenshaemoe_yravnenie, "=", otvet
                        print u"Ответ: ", otvet

                    else:

                        if vichitaemoe_yravnenie == "!":

                            otvet = ymenshaemoe_yravnenie - raznost_yravnenie
                            print
                            print ymenshaemoe_yravnenie, znak, vichitaemoe_yravnenie, "=", raznost_yravnenie
                            print vichitaemoe_yravnenie, "=", ymenshaemoe_yravnenie, znak, raznost_yravneni
                            print vichitaemoe_yravnenie, "=", otvet
                            print u"Ответ: ", otvet


def ABOUT():

    print
    print u"-=-=-=-= MathsHelper =-=-=-=-"
    print
    print u"Вы используете версию: v1.0 - Beta"
    print
    print u"Разработчик: Максим Батарон."
    print
    print u"Связаться с разработчиком: bataron.k69@gmail.com"
    print
    print u"YouTube-канал разработчика: https://www.youtube.com/channel/UCprG8OTWg8CPOhdUoDCBdlg"
    print
    print u"Copyright © 2018"

                    
#Start

print u"ВНИМАНИЕ! НА ДАННЫЙ МОМЕНТ ВЫ ИСПОЛЬЗУЕТЕ BETA-ВЕРСИЮ ПРОГРАММЫ!"
print
print u"======================================================"
print u"Добро пожаловать в MathsHelper!"
print u"Эта программа поможет вам с математическими расчетами!"
print u"Введите цифру интересующей вас функции."
print u"======================================================"
time.sleep(0.5)
while True:

    print
    print u"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
    print u"1 - Вычислить периметр."
    print u"2 - Вычислить площадь."
    print u"3 - Вычислить объём."
    print u"4 - Конвертер величин."
    print u"5 - Решить уравнение (простое)."
    print u"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
    print u"A - Просмотр информации о программе."
    print u"Для выхода введите любой другой символ."
    print u"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
    time.sleep(0.5)
    print
    print u"Номер функции: ",
    Function = raw_input()
    if Function == "1":

        Perimetr()

    else:

        if Function == "2":

            Ploshad()

        else:

            if Function == "3":

                Obyem()

            else:

                if Function == "4":

                    Konverter_velichin()

                else:   
               
                    if Function == "5":

                        Reshatel_yravnenii()

                    else:

                        if Function == "A" or Function == "a":

                            ABOUT()

                        else:

                            exit()


