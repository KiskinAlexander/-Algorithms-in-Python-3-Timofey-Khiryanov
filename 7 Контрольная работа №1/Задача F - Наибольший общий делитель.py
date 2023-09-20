# Необходимо найти НОД двух чисел, используя алгоритм Евклида.
# Ввод: 30\n18 Вывод: 6
# Ввод: 1071\n462 Вывод: 21

a = int(input())
b = int(input())


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


print(gcd(a, b))
