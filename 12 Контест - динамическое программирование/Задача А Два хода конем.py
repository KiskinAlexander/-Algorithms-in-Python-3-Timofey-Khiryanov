# Вам даны 2 координаты 2 клеток на шахматном поле. Нужно ответить на вопрос, можно ли попасть из одной клетки
# в другую за не более чем 2 хода конем. В случае, если попасть возможно, надо вывести количество ходов,
# за которое это можно сделать. Если попасть невозможно, следует вернуть -1.
# Ввод: 1\n1\n2\n3 Вывод: 1
# Ввод: 1\n1\n8\n8 Вывод: -1
def reset_el(A, N, M, c):
    # Ставим 1 если в клетку можно походить конём
    for i in (-2, +1), (-1, +2), (+1, +2), (+2, +1), (+2, -1), (+1, -2), (-1, -2), (-2, -1):
        if N + i[0] > -1 and N + i[0] < 8 and M + i[1] > -1 and M + i[1] < 8:
            A[N + i[0]][M + i[1]] = c


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
A = [[0] * 8 for i in range(8)]
reset_el(A, y1 - 1, x1 - 1, 1)
# второй проход
for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i - 1][j - 1] == 1:
            reset_el(A, i - 1, j - 1, 2)
if x1 == x2 and y1 == y2:
    print('-1')
elif A[y2 - 1][x2 - 1] == 2:
    print('2')
elif A[y2 - 1][x2 - 1] == 1:
    print('1')
else:
    print('-1')

'''# распечатка матрицы
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=' ')
    print()'''
