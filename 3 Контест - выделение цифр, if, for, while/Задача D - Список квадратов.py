# По данному натуральному числу N распечатайте все квадраты натуральных чисел, не превосходящие N ,
# в порядке возрастания.
# На вход программе передается целое число N , не превышающее 10000.
# Ввод: 50 Вывод 1 4 9 16 25 36 49
N = int(input())
i = 1

while True:
    if i**2 > N:
        break
    else:
        print(i**2, end=' ')
        i += 1
