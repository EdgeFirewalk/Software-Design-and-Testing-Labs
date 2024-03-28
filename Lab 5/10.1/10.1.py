# Программу написал:
# Лубенский Игорь Викторович
# Студент группы ПИН-222
# Задание 10.1

import sys

def init():
    global p, r
    p = [i for i in range(51)]
    r = [1 for _ in range(51)]

def find(x):
    if x == p[x]:
        return x
    p[x] = find(p[x])
    return p[x]

def joint(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        if r[x] > r[y]:
            r[x] += r[y]
            p[y] = x
        else:
            r[y] += r[x]
            p[x] = y
        return 1
    return 0

def dfs(node):
    for i in range(1, 51):
        if color_map[node][i]:
            color_map[node][i] -= 1
            color_map[i][node] -= 1
            dfs(i)
            print(i, node)

with open('input.txt', 'r') as f:
    t = int(f.readline().strip())
    test_case = 0
    while t > 0:
        t -= 1
        n = int(f.readline().strip())
        color_map = [[0 for _ in range(51)] for _ in range(51)]
        deg = [0 for _ in range(51)]
        init()
        for _ in range(n):
            x, y = map(int, f.readline().strip().split())
            color_map[x][y] += 1
            color_map[y][x] += 1
            deg[x] += 1
            deg[y] += 1
            joint(x, y)
        print("Case #{}".format(test_case + 1))
        test_case += 1
        st = -1
        flag = 0
        for i in range(1, 51):
            if deg[i] > 0:
                st = i
                if deg[i] & 1:
                    flag = 1
        for i in range(1, 51):
            if deg[i] > 0:
                if find(st) != find(i):
                    flag = 1
        if flag:
            print("Impossibleee")
        else:
            dfs(st)
        if t > 0:
            print()
