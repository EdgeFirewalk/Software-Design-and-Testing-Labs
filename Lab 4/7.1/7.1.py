

import sys
from math import fabs

class Status:
    def __init__(self):
        self.board = [[0]*4 for _ in range(4)]
        self.ix, self.iy = 0, 0

init = Status()
pos = [[0, 0] for _ in range(16)]
mxdep = 0
dir = [[0,-1],[-1,0],[1,0],[0,1]]
dirc = ['L', 'U', 'D', 'R']
path = ['\0']*100
solved = 0

def solvable():
    sum = 0
    row = 0
    for i in range(16):
        if(init.board[i//4][i%4] == 0):
            row = i//4 + 1
            continue
        for j in range(i+1, 16):
            if(init.board[j//4][j%4] < init.board[i//4][i%4]):
                if(init.board[j//4][j%4]):
                    sum += 1
    return 1-(sum+row)%2

def H():
    sum = 0
    for i in range(4):
        for j in range(4):
            num = init.board[i][j]
            if(num == 0):
                continue
            sum += abs(i-pos[num][0]) + abs(j-pos[num][1])
    return sum

Htable = [[[0]*16 for _ in range(4)] for _ in range(4)]

def IDA(dep, hv, prestep):
    global init, mxdep, solved, path
    if hv == 0:
        solved = dep
        print(''.join(path[:dep]))
        return dep
    if dep + 5 * hv // 3 > mxdep or dep >= 50:
        return dep + 5 * hv // 3
    for i in range(4):
        if i + prestep == 3:
            continue
        tx, ty = init.ix + dir[i][0], init.iy + dir[i][1]
        if tx < 0 or ty < 0 or tx > 3 or ty > 3:
            continue
        shv = hv
        shv -= Htable[tx][ty][init.board[tx][ty]]
        shv += Htable[init.ix][init.iy][init.board[tx][ty]]
        init.board[init.ix][init.iy], init.board[tx][ty] = init.board[tx][ty], init.board[init.ix][init.iy]
        init.ix, init.iy = tx, ty
        path[dep] = dirc[i]
        val = IDA(dep + 1, shv, i)
        init.board[init.ix][init.iy], init.board[tx][ty] = init.board[tx][ty], init.board[init.ix][init.iy]
        init.ix, init.iy = tx - dir[i][0], ty - dir[i][1]
        if solved:
            return solved
    return val

def main():
    global init, pos, mxdep, solved, path
    with open('input.txt', 'r') as f:
        test = int(f.readline().strip())
        pos = [None] + [[i, j] for i in range(4) for j in range(4)]
        for i in range(4):
            for j in range(4):
                for k in range(1, 16):
                    Htable[i][j][k] = abs(i - pos[k][0]) + abs(j - pos[k][1])
        while(test > 0):
            for i in range(4):
                line = f.readline().strip()
                init.board[i] = list(map(int, line.split()))
                for j in range(4):
                    if(init.board[i][j] == 0):
                        init.ix, init.iy = i, j
            if(solvable()):
                solved = 0
                initH = mxdep = H()
                if(not mxdep):
                    print("")
                    continue
                path = ['\0'] * 100
                while(solved == 0):
                    mxdep = IDA(0, initH, -1)
            else:
                print("This puzzle is not solvable.")
            test -= 1

if __name__ == "__main__":
    main()