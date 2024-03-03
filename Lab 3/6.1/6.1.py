# Программу написал:
# Лубенский Игорь Викторович
# Студент группы ПИН-222
# Задание 6.1

def fibonacci(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def count_fibonacci_in_range(a, b):
    fib_numbers = fibonacci(b)
    return len([num for num in fib_numbers if a <= num <= b])

def main():
    with open('input.txt', 'r') as file:
        for line in file:
            a, b = map(int, line.strip().split())
            if a == b == 0:
                break
            print(count_fibonacci_in_range(a, b))

if __name__ == "__main__":
    main()
