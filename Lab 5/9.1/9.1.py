# Программу написал:
# Лубенский Игорь Викторович
# Студент группы ПИН-222
# Задание 9.1

import sys

class Bus:
    def __init__(self, u, v, limit):
        self.u = u
        self.v = v
        self.limit = limit

def get_group(groups, u):
    if groups[u] == u:
        return u
    return get_group(groups, groups[u])

def main(input_file):
    Case = 1
    with open(input_file, 'r') as f:
        for line in f:
            N, R = map(int, line.split())
            if N == 0 and R == 0:
                break

            buses = []
            groups = list(range(N + 1))

            for i in range(R):
                bus = Bus(*map(int, f.readline().split()))
                bus.limit -= 1  # Мистеру Ж тоже нужно место
                buses.append(bus)

            S, D, T = map(int, f.readline().split())

            buses.sort(key=lambda s: s.limit, reverse=True)

            for i in range(R):
                bus = buses[i]
                group_u = get_group(groups, bus.u)
                group_v = get_group(groups, bus.v)
                if group_u != group_v:
                    groups[group_v] = group_u
                    if get_group(groups, S) == get_group(groups, D):
                        print(f"Scenario #{Case}\n"
                              f"Minimum Number of Trips = {(T + bus.limit - 1) // bus.limit}\n")
                        Case += 1
                        break

if __name__ == "__main__":
    main("input.txt")
