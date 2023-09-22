# Напишите функцию calculate_min_cost(n, price) вычисления наименьшей стоимость достижения клетки n из клетки 1
def count_min_cost(n, price):
    # В точку 1 можно попать только из точки 0
    c = [0] * (n+1)
    c[0] = price[0]
    c[1] = c[0] + price[1]
    for i in range(2, n+1):
        c[i] = price[i] + min(c[i - 1], c[i - 2])
    return c

f = int(input('Введите n:'))
s = input('Введите последовательность стоимостей клеток (n+1) штук:')
values = [int(x) for x in s.split(' ')]
print(count_min_cost(f, values))
