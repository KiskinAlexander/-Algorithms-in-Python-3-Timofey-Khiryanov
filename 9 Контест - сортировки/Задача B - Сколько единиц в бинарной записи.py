# Найти, сколько единиц содержит бинарная запись числа.
# Ввод: 5 Вывод: 2

n = int(input())
b = ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2
s = 0
for i in range(len(b)):
    if b[i] == '1':
        s += 1
print(s)
