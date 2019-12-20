#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

# Wersja z tablica każdy element oblicza tylko raz
# Rekurencyjna wersja każdy element środkowy bedzie obliczać nadmiernie dużo razy
# np żeby obliczyć P(4, 4) element P(1, 1) zostanie obliczony 20 razy

def P(i, j):
    P = [[0] * (j+1) for b in range(i+1)]
    P[0][0] = 0.5
    for a in range(0, i+1):
        for b in range(0, j+1):
            if a > 0 or b >0:
                if b == 0:
                    P[a][b] = 0.0
                elif a == 0:
                    P[a][b] = 1.0
                else:
                    P[a][b] = 0.5 * (P[a-1][b] + P[a][b-1])
    print (P)
    return P[i][j]

    # if i == 0 and j == 0:
    #     return 0.5
    # elif j == 0 and i > 0:
    #     return 0.0
    # elif i == 0 and j > 0:
    #     return 1.0
    # elif j > 0 and i > 0 :
    #     return 0.5 * (P(i-1, j) + P(i, j-1))

print (P(0, 0))
print (P(2, 0))
print (P(0, 2))
print (P(4, 2))

# 0.5
# 0.0   
# 1.0   
# 0.1875
