# В первой строке задается натуральное N<=10000 , длина массива, далее идут N чисел 0 или 1 -- элементы массива.
# Необходимо найти максимальное количество 1, идущих подряд (без 0 между ними).
# Ввод: 4\n1\n1\n0\n1 Вывод: 2

N = int(input())
t = 0
max1 = 0
for i in range(0, N):
    x = int(input())
    if x == 1:
        t += 1
    else:
        t = 0
    if t > max1:
        max1 = t
print(max1)
