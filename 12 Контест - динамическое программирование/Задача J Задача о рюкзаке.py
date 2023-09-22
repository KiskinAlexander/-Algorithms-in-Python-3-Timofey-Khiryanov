# Дано N предметов. Каждый из них имеет вес w i и стоимость p i . Также имеется рюкзак вместимостью W. От вас требуется
# найти такой набор предметов, что их суммарная стоимость максимальна, а суммарный вес не превосходит вместимость
# рюкзака. Ответом на задау надо будет вывести стоимость такого набора.
# На первых двух строках даны натуральные числа N и W, не превосходящие 100. На следующих 2*M строках даны пары чисел
# натуральных w i ≤ 100 и p i ≤ 1000.
# Ввод:5\n13\n3\n1\n4\n6\n5\n4\n8\n7\n9\n6 Вывод:13
n = int(input(''))
K = int(input(''))
l = 1
W = [0]
P = [0]
for i in range(2 * n):
    if l == 1:
        W.append(int(input()))
        l *= -1
    else:
        if l == -1:
            P.append(int(input()))
            l *= -1

F = [[0] * (K + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for k in range(1, K + 1):
        if k >= W[i]:
            F[i][k] = max(F[i - 1][k], F[i - 1][k - W[i]] + P[i])
        else:
            F[i][k] = F[i - 1][k]

k = K
Ans = []
k = K
for i in range(n, 0, -1):
    if F[i][k] != F[i - 1][k]:
        Ans.append(i)
        k -= W[i]
# print(*Ans)
sum1 = 0
for i in range(len(Ans)):
    sum1 += P[Ans[i]]
print(sum1)
# print(*Ans)
