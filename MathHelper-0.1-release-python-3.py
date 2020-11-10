## Дорогой программист:
## Когда я писал этот код, только
## я и бог знали, как он работает.
## Теперь знает только бог!
##
## Если ты попытаешься что-нибудь
## здесь оптимизировать и у тебя
## не получится (скорее всего),
## то увеличь значение счётчика,
## как предупреждение для следующего
## человека:
##
## kolichestvo_chasov_potrachennih_zdec' = 1
##
##Peremennie

metr = "м"

kilometr = "км"
mm = "мм"
dc = "дм"
kg = "кг"
centneri = "ц"
gramm = "г"
tonna = "т"


import time



def Perimetr():
    print("ВНИМАНИЕ! Если вам нужно ввести десятичную дробь, то используйте ТОЧКУ для разделения целой и десятичной части!")
    print()
    shirina = float(input("Введите ширину(см): "))
    dlina = float(input("Введите длину(см): "))
    if shirina > dlina:
        print("Ошибка: ширина не может быть больше длины! Попробуйте повторить попытку.")
    elif shirina < dlina or shirina == dlina:
        rezyltat_perimetr = dlina + shirina + dlina + shirina
        print("Ответ: ", rezyltat_perimetr, " сантиметров.")
def Ploshad():
    print("ВНИМАНИЕ! Если вам нужно ввести десятичную дробь, то используйте ТОЧКУ для разделения целой и десятичной части!")
    print()
    shirina = float(input("Введите ширину(см): "))
    dlina = float(input("Введите длину(см): "))
    if shirina > dlina:
        print ("Ошибка: ширина не может быть больше длины! Попробуйте повторить попытку.")
    elif shirina < dlina or shirina == dlina:
        rezyltat_ploshad = dlina * shirina
        print("Ответ: ", rezyltat_ploshad, " сантиметров в квадрате.")
def Obyem():
    print("ВНИМАНИЕ! Если вам нужно ввести десятичную дробь, то используйте ТОЧКУ для разделения целой и десятичной части!")
    print()
    shirina = float(input("Введите ширину(см): "))
    dlina =  float(input("Введите длину(см): "))
    visota = float(input("Введите высоту(см): "))
    if shirina > dlina:
        print("Ошибка: ширина не может быть больше длины! Попробуйте повторить попытку.")
    elif shirina < dlina or shirina == dlina:
        rezyltat_obyem = dlina * shirina * visota
        print("Ответ: ", rezyltat_obyem, " сантиметров в кубе.")
def Konverter_velichin():
    time.sleep(0.5)
    print("ВНИМАНИЕ! Если вам нужно ввести десятичную дробь, то используйте ТОЧКУ для разделения целой и десятичной части!")
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
        print ("Ответ: ", znachenie_velichini)
    else:
        if tip_velichini == "4" and konechnii_tip_velichini == "2":
            
            otvet = znachenie_velichini * 100
            print()
            print ("Ответ: ", otvet)
        else:                                
            
    	    if tip_velichini == "1" and konechnii_tip_velichini == "2":
                

                otvet = znachenie_velichini / 10
                print()
                print ("Ответ: ", otvet)

            else:

                if tip_velichini == "5" and konechnii_tip_velichini == "2":
        	    otvet = znachenie_velichini * 1000000
        	    print()
        	    print ("Ответ: ", otvet)
        	    
   		else:
                    
   		    if tip_velichini == "3" and konechnii_tip_velichini == "2":
        	        otvet = znachenie_velichini * 10
        		print()
        		print ("Ответ: ", otvet) 
    		    else:
    			if tip_velichini == "2" and konechnii_tip_velichini == "1":
        		    otvet = znachenie_velichini * 10
        		    print() 
        		    print ("Ответ: ", otvet) 
                        else:

                            if tip_velichini == "4" and konechnii_tip_velichini == "1":

                                otvet = znachenie_velichini * 1000
                                print()
                                print ("Ответ: ", otvet) 

                            else:

                                if tip_velichini == "1" and konechnii_tip_velichini == "1":

                                    print()
                                    print ("Ответ: ", znachenie_velichini)

                                else:

                                    if tip_velichini == "5" and konechnii_tip_velichini == "1":

                                        otvet = znachenie_velichini * 10000000
                                        print()
                                        print ("Ответ: ", otvet) 

                                    else:

                                        if tip_velichini == "3" and konechnii_tip_velichini == "1":

                                            otvet = znachenie_velichini * 100
                                            print()
                                            print ("Ответ: ", otvet) 

                                        else:

                                            if tip_velichini == "2" and konechnii_tip_velichini == "4":

                                                otvet = znachenie_velichini / 100
                                                print()
                                                print ("Ответ: ", otvet) 

                                            else:

                                                if tip_velichini == "4" and konechnii_tip_velichini == "4":

                                                    print()
                                                    print ("Ответ: ", znachenie_velichini) 

                                                else:

                                                    if tip_velichini == "1" and konechnii_tip_velichini == "4":

                                                        otvet = znachenie_velichini / 1000
                                                        print()
                                                        print ("Ответ: ", otvet) 

                                                    else:

                                                        if tip_velichini == "5" and konechnii_tip_velichini == "4":

                                                            otvet = znachenie_velichini / 1000
                                                            print()
                                                            print ("Ответ: ", otvet) 

                                                        else:

                                                            if tip_velichini == "3" and konechnii_tip_velichini == "4":

                                                                otvet = znachenie_velichini / 10
                                                                print()
                                                                print ("Ответ: ", otvet) 

                                                            else:                                                                                        

                                                                if tip_velichini == "2" and konechnii_tip_velichini == "3":

                                                                    otvet = znachenie_velichini / 10
                                                                    print()
                                                                    print ("Ответ: ", znachenie_velichini)

                                                                else:

                                                                    if tip_velichini == "4" and konechnii_tip_velichini == "3":

                                                                        otvet = znachenie_velichini / 10
                                                                        print()
                                                                        print ("Ответ: ", otvet) 

                                                                    else:

                                                                        if tip_velichini == "1" and konechnii_tip_velichini == "3":

                                                                            otvet = znachenie_velichini / 10
                                                                            print()
                                                                            print ("Ответ: ", otvet) 

                                                                        else:

                                                                            if tip_velichini == "5" and konechnii_tip_velichini == "3":

                                                                                otvet = znachenie_velichini / 10
                                                                                print()
                                                                                print ("Ответ: ", otvet) 

                                                                            else:

                                                                                if tip_velichini == "3" and konechnii_tip_velichini == "3":

                                                                                    print()
                                                                                    print ("Ответ: ", znachenie_velichini)                                                   

                                                                                else:     #kilometri

                                                                                    if tip_velichini == "2" and konechnii_tip_velichini == "5":

                                                                                        otvet = znachenie_velichini / 1000000
                                                                                        print()
                                                                                        print ("Ответ: ", otvet) 

                                                                                    else:

                                                                                        if tip_velichini == "4" and konechnii_tip_velichini == "5":

                                                                                            otvet = znachenie_velichini / 1000
                                                                                            print()
                                                                                            print ("Ответ: ", otvet) 

                                                                                        else:

                                                                                            if tip_velichini == "1" and konechnii_tip_velichini == "5":

                                                                                                otvet = znachenie_velichini / 10000000
                                                                                                print()
                                                                                                print ("Ответ: ", otvet) 

                                                                                            else:

                                                                                                if tip_velichini == "5" and konechnii_tip_velichini == "5":
                                                                                                                                                                    
                                                                                                    print()
                                                                                                    print ("Ответ: ", znachenie_velichini) 

                                                                                                else:

                                                                                                    if tip_velichini == "3" and konechnii_tip_velichini == "5":

                                                                                                        otvet = znachenie_velichini / 100
                                                                                                        print()
                                                                                                        print ("Ответ: ", otvet) 

                                                                                                    else:

                                                                                                                                                                        
                                                                                                        if tip_velichini == "6" and konechnii_tip_velichini == "6":

                                                                                                            print()
                                                                                                            print ("Ответ: ", znachenie_velichini)

                                                                                                        else:

                                                                                                            if tip_velichini == "6" and konechnii_tip_velichini == "7":

                                                                                                                otvet = znachenie_velichini / 1000
                                                                                                                print()
                                                                                                                print ("Ответ: ", otvet)

                                                                                                            else:

                                                                                                                if tip_velichini == "6" and konechnii_tip_velichini == "8":

                                                                                                                    otvet = znachenie_velichini / 100000
                                                                                                                    print()
                                                                                                                    print ("Ответ: ", otvet)

                                                                                                                else:

                                                                                                                    if tip_velichini == "6" and konechnii_tip_velichini == "9":

                                                                                                                        otvet = znachenie_velichini / 1000000
                                                                                                                        print()
                                                                                                                        print ("Ответ: ", otvet)

                                                                                                                    else:

                                                                                                                        if tip_velichini == "7" and konechnii_tip_velichini == "6":

                                                                                                                            otvet = znachenie_velichini * 1000
                                                                                                                            print()
                                                                                                                            print ("Ответ: ", otvet)

                                                                                                                        else:

                                                                                                                            if tip_velichini == "7" and konechnii_tip_velichini == "7":

                                                                                                                                print()
                                                                                                                                print ("Ответ: ", znachenie_velichini)

                                                                                                                            else:

                                                                                                                                if tip_velichini == "7" and konechnii_tip_velichini == "8":

                                                                                                                                    otvet = znachenie_velichini / 100
                                                                                                                                    print()
                                                                                                                                    print ("Ответ: ", otvet)

                                                                                                                                else:

                                                                                                                                    if tip_velichini == "7" and konechnii_tip_velichini == "9":

                                                                                                                                        otvet = znachenie_velichini / 1000
                                                                                                                                        print()
                                                                                                                                        print ("Ответ: ", otvet)

                                                                                                                                    else:

                                                                                                                                        if tip_velichini == "8" and konechnii_tip_velichini == "6":

                                                                                                                                            otvet = znachenie_velichini * 100000
                                                                                                                                            print()
                                                                                                                                            print ("Ответ: ", otvet)

                                                                                                                                        else:

                                                                                                                                            if tip_velichini == "8" and konechnii_tip_velichini == "7":

                                                                                                                                                otvet = znachenie_velichini * 100
                                                                                                                                                print()
                                                                                                                                                print ("Ответ: ", otvet)

                                                                                                                                            else:

                                                                                                                                                if tip_velichini == "8" and konechnii_tip_velichini == "8":

                                                                                                                                                    print()
                                                                                                                                                    print ("Ответ: ", znachenie_velichini)

                                                                                                                                                else:

                                                                                                                                                    if tip_velichini == "8" and konechnii_tip_velichini == "9":

                                                                                                                                                        otvet = znachenie_velichini / 10
                                                                                                                                                        print()
                                                                                                                                                        print ("Ответ: ", otvet)

                                                                                                                                                    else:

                                                                                                                                                        if tip_velichini == "9" and konechnii_tip_velichini == "6":

                                                                                                                                                            otvet = znachenie_velichini * 1000000
                                                                                                                                                            print()
                                                                                                                                                            print ("Ответ: ", otvet)

                                                                                                                                                        else:

                                                                                                                                                            if tip_velichini == "9" and konechnii_tip_velichini == "7":
                                                                                                                                                                                                                                    
                                                                                                                                                                otvet = znachenie_velichini * 1000
                                                                                                                                                                print()
                                                                                                                                                                print ("Ответ: ", otvet)

                                                                                                                                                            else:

                                                                                                                                                                if tip_velichini == "9" and konechnii_tip_velichini == "8":

                                                                                                                                                                    otvet = znachenie_velichini * 10
                                                                                                                                                                    print()
                                                                                                                                                                    print ("Ответ: ", otvet)

                                                                                                                                                                else:

                                                                                                                                                                    if tip_velichini == "9" and konechnii_tip_velichini == "9":
                                                                                                                                                                                                     
                                                                                                                                                                        print()
                                                                                                                                                                        print ("Ответ: ", znachenie_velichini)

                                                                                                                                                                    else:

                                                                                                                                                                        print()
                                                                                                                                                                        print ("Ошибка конвертации! Попробуйте повторить попытку.")
                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                        
def Reshatel_yravnenii():

    print()
    print ("1 - умножение")
    print ("2 - деление")
    print ("3 - сложение")
    print ("4 - вычитание")
    print ("Какое действие является основным в уравнении: ")
    deistvie_yravnenie = str(input())
    print()
    if deistvie_yravnenie == "1":
        znak = "×"
        print()
        first_mnojitel = str(input("Введите значение первого множителя (если является корнем уравнения, то введите '!'): "))
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
        print ("Введите значение произведения: ")
        proizvedenie = float(input())
        if first_mnojitel == "!":
            otvet = proizvedenie / second_mnojitel
            print()
            print ("X", znak, second_mnojitel, "=", proizvedenie)
            print ("X", "=", proizvedenie, ":", second_mnojitel)
            print ("X", "=", otvet)
            print ("Ответ: ", otvet)
        elif second_mnojitel == "!":
            otvet = proizvedenie / first_mnojitel
            print()
            print (first_mnojitel, znak, "X", "=", proizvedenie)
            print ("X", "=", proizvedenie, ":", first_mnojitel)
            print ("X", "=", otvet)
            print ("Ответ: ", otvet)
    else:
        if deistvie_yravnenie == "3":
            znak = "+"
            print()
            print ("Введите значение первого слагаемого (если является корнем уравнения, то введите !): ")
            first_slagaemoe = str(input())
            if first_slagaemoe == "!":
                first_slagaemoe = str(first_slagaemoe)
            else:
                first_slagaemoe = float(first_slagaemoe)
            print()
            print ("Введите значение второго слагаемого (если является корнем уравнения, то введите !): ")
            second_slagaemoe = str(input())
            if second_slagaemoe == "!":
                second_slagaemoe = str(second_slagaemoe)
            else:
                second_slagaemoe = float(second_slagaemoe)
            print()
            print ("Введите значение суммы: ")
            symma_yravnenie = float(input())
            if first_slagaemoe == "!":
                print()
                otvet = symma_yravnenie - second_slagaemoe
                print()
                print (first_slagaemoe, znak, second_slagaemoe, "=", symma_yravnenie)
                print (first_slagaemoe, "=", symma_yravnenie, "-", second_slagaemoe)
                print (first_slagaemoe, "=", otvet)
                print ("Ответ: ", otvet)

            else:

                if second_slagaemoe == "!":

                    print()
                    otvet = symma_yravnenie - first_slagaemoe
                    print()
                    print (first_slagaemoe, znak, second_slagaemoe, "=", symma_yravnenie)
                    print (second_slagaemoe, "=", symma_yravnenie, "-", first_slagaemoe)
                    print ("Ответ: ", otvet)

        else:

            if deistvie_yravnenie == "2":

                znak = ":"
                print()
                print ("Введите значение делимого (если является корнем уравнения, то введите !): ")
                delimoe_yravnenie = str(input())
                if delimoe_yravnenie == "!":

                    delimoe_yravnenie = str(delimoe_yravnenie)

                else:

                    delimoe_yravnenie = float(delimoe_yravnenie)

                print()
                print ("Введите значение делителя (если является корнем уравнения, то введите !): ")
                delitel_yravnenie = str(input())
                if delitel_yravnenie == "!":

                    delitel_yravnenie == str(delitel_yravnenie)

                else:

                    delitel_yravnenie == float(delitel_yravnenie)

                print()
                print ("Введите значение частного: ")
                chastnoe_yravnenie = str(input())
                if delimoe_yravnenie == "!":

                    print()
                    otvet = chastnoe_yravnenie / delitel_yravnenie
                    print (delimoe_yravnenie, znak, delitel_yravnenie, "=", chastnoe_yravnenie)
                    print (delimoe_yravnenie, "=", chastnoe_yravnenie, znak, delitel_yravnenie)
                    print ("Ответ: ", otvet)

                else:

                    if delitel_yravnenie == "!":

                        otvet = chastnoe_yravnenie / delimoe_yravnenie
                        print()
                        print (delimoe_yravnenie, znak, delitel_yravnenie, "=", chastnoe_yravnenie)
                        print (delitel_yravnenie, "=", chastnoe_yravnenie, znak, delimoe_yravnenie)
                        print ("Ответ: ", otvet)

            else:

                if deistvie_yravnenie == "4":

                    znak = "-"
                    print()
                    print ("Введите значение уменьшаемого (если является корнем уравнения, то введите !): ")
                    ymenshaemoe_yravnenie = str(input())
                    if ymenshaemoe_yravnenie == "!":

                        ymenshaemoe_yravnenie = str(ymenshaemoe_yravnenie)

                    else:

                        ymenshaemoe_yravnenie = float(ymenshaemoe_yravnenie)

                    print()
                    print ("Введите значение вычитаемого (если является корнем уравнения, то введите !): ")
                    vichitaemoe_yravnenie = str(input())
                    if vichitaemoe_yravnenie == "!":

                        vichitaemoe_yravnenie = str(vichitaemoe_yravnenie)

                    else:

                        vichitaemoe_yravnenie = float(vichitaemoe_yravnenie)

                    print()
                    print ("Введите значение разности: ")
                    raznost_yravnenie = str(input())
                    print()
                    if ymenshaemoe_yravnenie == "!":

                        otvet = vichitaemoe_yravnenie + raznost_yravnenie
                        print()
                        print (ymenshaemoe_yravnenie, znak, vichitaemoe_yravnenie, "=", raznost_yravnenie)
                        print (ymenshaemoe_yravnenie, "=", raznost_yravnenie, "+", vichitaemoe_yravnenie)
                        print (ymenshaemoe_yravnenie, "=", otvet)
                        print ("Ответ: ", otvet)

                    else:

                        if vichitaemoe_yravnenie == "!":

                            otvet = ymenshaemoe_yravnenie - raznost_yravnenie
                            print()
                            print (ymenshaemoe_yravnenie, znak, vichitaemoe_yravnenie, "=", raznost_yravnenie)
                            print (vichitaemoe_yravnenie, "=", ymenshaemoe_yravnenie, znak, raznost_yravnenie)
                            print (vichitaemoe_yravnenie, "=", otvet)
                            print ("Ответ: ", otvet)


def ABOUT():

    print()
    print ("-=-=-=-= MathsHelper =-=-=-=-")
    print()
    print ("Вы используете версию: v1.0 - Beta")
    print()
    print ("Разработчик: Максим Батарон.")
    print()
    print ("Связаться с разработчиком: di0nik.gd@gmail.com")
    print()
    print ("YouTube-канал разработчика: https://www.youtube.com/channel/UCprG8OTWg8CPOhdUoDCBdlg")
    print()
    print ("Copyright © 2020")

                    

print ("ВНИМАНИЕ! НА ДАННЫЙ МОМЕНТ ВЫ ИСПОЛЬЗУЕТЕ BETA-ВЕРСИЮ ПРОГРАММЫ!")
print()
print ("======================================================")
print ("Добро пожаловать в MathsHelper!")
print ("Эта программа поможет вам с математическими расчетами!")
print ("Введите цифру интересующей вас функции.")
print ("======================================================")
while True:
    print()
    print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print ("1 - Вычислить периметр.")
    print ("2 - Вычислить площадь.")
    print ("3 - Вычислить объём.")
    print ("4 - Конвертер величин.")
    print ("5 - Решить уравнение (простое).")
    print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print ("A - Просмотр информации о программе.")
    print ("Для выхода введите любой другой символ.")
    print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print()
    print ("Номер функции: ")
    Function = str(input())
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
