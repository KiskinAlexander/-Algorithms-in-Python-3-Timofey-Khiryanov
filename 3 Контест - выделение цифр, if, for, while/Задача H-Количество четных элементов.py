# Посчитать количество четных элементов в массиве целых чисел, заканчивающихся нулём. Сам ноль учитывать не надо.
# Ввод: 1\n2\n0 Вывод: 1
i = 0
while True:
    N = int(input())
    if N == 0:
        break
    if N % 2 == 0:
        i += 1
print(i)
