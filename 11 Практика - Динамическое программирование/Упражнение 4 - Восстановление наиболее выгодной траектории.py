def count_min_cost(n, price):
    # В точку 1 можно попать только из точки 0
    c = [0] * (n+1)
    c[0] = price[0]
    c[1] = c[0] + price[1]
    for i in range(2, n+1):
        c[i] = price[i] + min(c[i - 1], c[i - 2])
    # идём по массиву с конца и кладём наиболее выгодные траектории
    Path = [n]
    while Path[-1] != 0:
        i = Path[-1]
        if c[i - 1] < c[-2]:
            Path.append(i - 1)
        else:
            Path.append(i - 2)
    Path = Path[::-1]

    print(Path)


f = int(input('Введите n:'))
s = input('Введите последовательность стоимостей клеток (n+1) штук:')
values = [int(x) for x in s.split(' ')]
count_min_cost(f, s)
