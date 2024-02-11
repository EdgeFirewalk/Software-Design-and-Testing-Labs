# Программу написал:
# Лубенский Игорь Викторович
# Студент группы ПИН-222
# Задание 1.1

filename = 'input_1.txt'

try:
    # Открываем файл с входными данными
    with open(filename, 'r') as file:
        for line in file:
            # Читаем файл построчно
            # Данные в каждой строке разделены пробелами
            inpt = line.strip().split(' ')

            try:
                # Проверяем, числа ли во входных данных
                i = int(inpt[0])
                j = int(inpt[1])
                
                # И находятся ли они в заданном диапазоне (0 - 1.000.000)
                if i <= 0 or j <= 0:
                    raise TypeError
            except ValueError:
                # Если во входных данных не числа
                print('Пожалуйста, введите целые неотрицательные i и j!')
                continue
            except TypeError:
                # Если входные данные не в заданном диапазоне
                print('Входные данные не находятся в диапазоне от 0 до 1.000.000!')
                continue

            max_length = 0
            for n in range(i, j + 1):
                current_number = n
                cycle_length = 1
                while current_number != 1:
                    if current_number % 2 == 0:
                        current_number = current_number / 2
                    else:
                        current_number = (current_number * 3) + 1
                    cycle_length += 1
                if cycle_length > max_length:
                    max_length = cycle_length
            
            print(inpt[0] + ' ' + inpt[1] + ' ' + str(max_length))
except FileNotFoundError:
    print(f'Файл с именем "{filename}" не найден...')
