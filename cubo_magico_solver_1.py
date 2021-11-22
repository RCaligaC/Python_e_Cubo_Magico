from random import choice, randint
# import os
from pycuber import solver
from pycuber import Cube

movimentos = [["R", "R'", "R2"],
              ["U", "U'", "U2"],
              ["B", "B'", "B2"],
              ["F", "F'", "F2"],
              ["L", "L'", "L2"],
              ["D", "D'", "D2"]]


def reducao(list):
    m1 = []
    for i in list:
        m1.append(choice(i))
    return m1


def escolha():
    var = randint(1, 6)
    return var


mov1 = escolha()
mov2 = escolha()
while mov2 == mov1:
    mov2 = escolha()
mov3 = escolha()
while mov3 == mov2:
    mov3 = escolha()
mov4 = escolha()
while mov4 == mov3:
    mov4 = escolha()
mov5 = escolha()
while mov5 == mov4:
    mov5 = escolha()
mov6 = escolha()
while mov6 == mov5:
    mov6 = escolha()
mov7 = escolha()
while mov7 == mov6:
    mov7 = escolha()
mov8 = escolha()
while mov8 == mov7:
    mov8 = escolha()
mov9 = escolha()
while mov9 == mov8:
    mov9 = escolha()
mov10 = escolha()
while mov10 == mov9:
    mov10 = escolha()
mov11 = escolha()
while mov11 == mov10:
    mov11 = escolha()
mov12 = escolha()
while mov12 == mov11:
    mov12 = escolha()
mov13 = escolha()
while mov13 == mov12:
    mov13 = escolha()
mov14 = escolha()
while mov14 == mov13:
    mov14 = escolha()
mov15 = escolha()
while mov15 == mov14:
    mov15 = escolha()
mov16 = escolha()
while mov16 == mov15:
    mov16 = escolha()
mov17 = escolha()
while mov17 == mov16:
    mov17 = escolha()
mov18 = escolha()
while mov18 == mov17:
    mov18 = escolha()
mov19 = escolha()
while mov19 == mov18:
    mov19 = escolha()

scramble_num = [mov1, mov2, mov3, mov4, mov5, mov6, mov7, mov8, mov9, mov10, mov11, mov12, mov13, mov14, mov15, mov16, mov17, mov18, mov19]

scramble = []
for i in scramble_num:
    s = reducao(movimentos)
    if i == 1:
        scramble.append(s[0])
    elif i == 2:
        scramble.append(s[1])
    elif i == 3:
        scramble.append(s[2])
    elif i == 4:
        scramble.append(s[3])
    elif i == 5:
        scramble.append(s[4])
    elif i == 6:
        scramble.append(s[5])

alg = " ".join(scramble)

def solve(list):
    c = Cube()(list)
    print(c)
    s = solver.CFOPSolver(c)
    s.solve()

print("Scramble: %s" % alg)
solve(alg)
