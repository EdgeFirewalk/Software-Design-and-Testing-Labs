# Программу написал:
# Лубенский Игорь Викторович
# Студент группы ПИН-222
# Задание 5.1

import sys

# Эта функция пытается присвоить значения n числам таким образом, чтобы их парные суммы совпадали с заданными данными
def do_assign(index, data, taken, results):
    # Базовый случай: Если индекс равен длине данных, это означает, что найдено допустимое присваивание
    if index == len(data):
        return True

    # Вычисляем положение опорного элемента на основе длины списка результатов
    pivot_loc = (len(results) - 1) * len(results) // 2

    # Проходим по данным, начиная с третьего элемента
    for i in range(2, len(data)):
        # Особый случай для первых двух индексов
        if index == 2:
            # Вычисляем среднее значение
            avd = (data[0] + data[1] - data[i]) / 2.0
            # Проверяем, является ли среднее значение целым числом
            if abs(avd - int(avd)) > 1e-8:
                continue
            # Добавляем вычисленные значения в результаты и помечаем текущий индекс как использованный
            results.append(int(avd))
            results.append(data[0] - int(avd))
            results.append(data[1] - int(avd))
            taken[i] = True
        # Особый случай для положения опорного элемента
        elif index == pivot_loc:
            # Пропускаем, если текущий индекс уже использован
            if taken[i]:
                continue
            # Добавляем вычисленное значение в результаты и помечаем текущий индекс как использованный
            results.append(data[i] - results[0])
            taken[i] = True
        else:
            # Вычисляем новое положение опорного элемента для неспециальных случаев
            pivot_loc = (len(results) - 2) * (len(results) - 1) // 2
            # Пропускаем, если текущий индекс уже использован
            if taken[i]:
                continue
            # Пропускаем, если текущий элемент данных не соответствует условию присваивания
            if data[i] - results[-1] != results[index % pivot_loc]:
                continue
            # Помечаем текущий индекс как использованный
            taken[i] = True

        # Рекурсивный вызов do_assign для следующего индекса
        if do_assign(index + 1, data, taken, results):
            return True

        # Откатываем текущее присваивание
        taken[i] = False
        # Сбрасываем результаты для первых двух индексов
        if index == 2:
            del results[:]
        # Удаляем последний результат для других индексов
        elif index == pivot_loc:
            results.pop()

    # Возвращаем False, если не найдено допустимое присваивание
    return False

def main():
    with open("input.txt", "r") as file:
        # Читаем каждую строку из файла
        for line in file:
            # Разделяем строку на список строк
            data_str = line.strip().split()
            # Преобразуем первую строку в целое число
            n = int(data_str[0])
            # Преобразуем остальные строки в целые числа
            data = list(map(int, data_str[1:]))
            # Вычисляем лимит на основе n
            limit = n * (n - 1) // 2

            # Проверяем, соответствует ли количество целых чисел ожидаемому лимиту
            if limit != len(data):
                print("Impossibleeee")
                continue

            # Сортируем данные
            data.sort()
            # Инициализируем списки результатов и использованных элементов
            results = []
            taken = [False] * limit

            # Вызываем do_assign для попытки найти допустимое присваивание
            if do_assign(2, data, taken, results):
                # Сортируем результаты и выводим их
                results.sort()
                print(*results)
            else:
                print("Impossibleeee")

main()
