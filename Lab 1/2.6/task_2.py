# Программу написал:
# Лубенский Игорь Викторович
# Студент группы ПИН-222
# Задание 2.6

def is_jolly(values, n):
    if n <= 0:
        return 'Not Jolly'

    seq = []
    for i in range(1, n-1):
        d = abs(values[i] - values[i + 1])
        if ((d > n-1) or (d == 0) or (d in seq)):
            return 'Not Jolly'
        else:
            seq.append(d)
            
    return 'Jolly'

# Открываем файл, читаем его построчно
with open('input.txt', 'r') as file:
    for line in file:
        parts = line.split(' ')
        try:
            n = int(parts[0]) # n — это первое число в строке
            sequence = list(map(int, parts[1:])) # остальные числа — последовательность
        except ValueError:
            print('Ошибка входных данных: содержатся не числовые данные')
            continue
        result = is_jolly(sequence, n)
        print(result)