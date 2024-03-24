# Дано трехзначное число. Найдите сумму его цифр.
# Пример: Ввод 179, Вывод 17
def sum1(a):
    sum_i = 0
    for i in a:
        sum_i+=int(i)
    return sum_i
A = input()
print(sum1(A))
