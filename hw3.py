
i = 0
base_number=0
input_number=0
while True:
    if i == 0:
        while True:
            base_number = input ('Введите первое число (Первый операнд): ')
            # try:
            #     checked_base_number = int(base_number)
            # except ValueError:
            #     print ('Not a number. Please, make it correct.')
            #     continue 
            # else:
            #     base_number = int(base_number)
            try:
                checked_base_number = float(base_number)
            except ValueError:
                print ('Not a number. Please, make it correct.')
                continue
            else:
                base_number = float(base_number)
            break
        i += 1
    else:
        while True:
            input_operator = input("Что нужно сделать с этим числом?  (СЛОЖЕНИЕ (+); ВЫЧИТАНИЕ (-); УМНОЖЕНИЕ (*); ДЕЛЕНИЕ (/); НИЧЕГО - СКАЖИТЕ РЕЗУЛЬТАТ (=))")
            if input_operator == "+" or input_operator == "-" or input_operator == "*" or input_operator == "/" or input_operator == "=":
                break
            else: 
                print ('Я не понимаю - могу dелать только СЛОЖЕНИЕ (+); ВЫЧИТАНИЕ (-); УМНОЖЕНИЕ (*); ДЕЛЕНИЕ (/) И УЗНАТЬ РЕЗУЛЬТАТ (=))')
                continue
        while True:
            if input_operator == '=':
                break
            input_number = input ('Введите следующее число: ')
            # try:
            #     checked_next_number = int(input_number)
            # except ValueError:
            #     print ('Not a number. Please, make it correct.')
            #     continue
            # else:
            #     base_number = int(input_number)
            try:
                checked_next_number = float(input_number)
            except ValueError:
                print ('Not a number. Please, make it correct.')
                continue 
            else:
                input_number = float(input_number)
            break
        if input_operator == '+':
            base_number = base_number + input_number
        elif input_operator == '-':
            base_number = base_number - input_number
        elif input_operator == '*':
            base_number = base_number * input_number
        elif input_operator == '/':
            if input_number == 0:
                print ("На ноль не могу поделить - давай сначала")
                continue
            else:
                base_number = base_number / input_number
        else:
            print ('Получилось: ', base_number)
            again_case = input('Хотите попробовать снова? (Y/N) ')
            while not (again_case == 'N' or again_case == 'n' or again_case == 'Y' or again_case == 'y'):
                again_case = input('Непонятно. Хотите попробовать снова? (Y/N)  ')
            if again_case == 'Y' or again_case == 'y':
                i = 0
                continue
            elif again_case == 'N' or again_case == 'n':
                break