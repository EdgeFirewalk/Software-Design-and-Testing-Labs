# Программу написал:
# Лубенский Игорь Викторович
# Студент группы ПИН-222
# Задание 5.1

import sys

def do_assign(index, data, taken, results):
    if index == len(data):
        return True

    pivot_loc = (len(results) - 1) * len(results) // 2

    for i in range(2, len(data)):
        if index == 2:
            avd = (data[0] + data[1] - data[i]) / 2.0
            if abs(avd - int(avd)) > 1e-8:
                continue
            results.append(int(avd))
            results.append(data[0] - int(avd))
            results.append(data[1] - int(avd))
            taken[i] = True
        elif index == pivot_loc:
            if taken[i]:
                continue
            results.append(data[i] - results[0])
            taken[i] = True
        else:
            pivot_loc = (len(results) - 2) * (len(results) - 1) // 2
            if taken[i]:
                continue
            if data[i] - results[-1] != results[index % pivot_loc]:
                continue
            taken[i] = True

        if do_assign(index + 1, data, taken, results):
            return True

        taken[i] = False
        if index == 2:
            del results[:]
        elif index == pivot_loc:
            results.pop()

    return False

def main():
    with open("input.txt", "r") as file:
        for line in file:
            data_str = line.strip().split()
            n = int(data_str[0])
            data = list(map(int, data_str[1:]))
            limit = n * (n - 1) // 2

            if limit != len(data):
                print("Impossibleeee")
                continue

            data.sort()
            results = []
            taken = [False] * limit

            if do_assign(2, data, taken, results):
                results.sort()
                print(*results)
            else:
                print("Impossibleeee")

if __name__ == "__main__":
    main()
