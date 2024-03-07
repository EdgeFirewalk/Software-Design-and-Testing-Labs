# Программу написал:
# Лубенский Игорь Викторович
# Студент группы ПИН-222
# Задание 6.1

def fibonacci(n):
    fib = [0, 1] # Инициализация списка с первыми двумя числами Фибоначчи
    while fib[-1] < n: # Пока последнее число в списке меньше n
        fib.append(fib[-1] + fib[-2]) # Добавляем следующее число Фибоначчи
    return fib # Возвращаем список чисел Фибоначчи

def count_fibonacci_in_range(a, b):
    fib_numbers = fibonacci(b) # Получаем список чисел Фибоначчи до b
    return len([num for num in fib_numbers if a <= num <= b]) # Возвращаем количество чисел в диапазоне [a, b]

def main():
    with open('input.txt', 'r') as file: # Открываем файл для чтения
        for line in file: # Читаем файл построчно
            a, b = map(int, line.strip().split()) # Разбиваем строку на числа a и b
            if a == b == 0: # Если оба числа равны 0, прерываем цикл
                break
            print(count_fibonacci_in_range(a, b)) # Выводим количество чисел Фибоначчи в диапазоне [a, b]

main()
