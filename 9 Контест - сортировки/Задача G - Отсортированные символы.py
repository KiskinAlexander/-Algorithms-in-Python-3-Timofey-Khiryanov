# Напечатайте входную строку, отсортировав ее по возрастанию ASCII кода символов.
# Ввод: qwe Rty5, yu! Mama. Вывод:  !,5MRaaemqtuwyy.
str = input()
x = []
top = 0
while top < len(str):
    if str[top] == '.':
        break
    x.append(ord(str[top]))
    top += 1


def sort(x):
    if len(x) <= 1:
        return
    barrier = x[0]
    left = []
    right = []
    middle = []
    for k in x:
        if k < barrier:
            left.append(k)
        elif k == barrier:
            middle.append(k)
        else:
            right.append(k)
    sort(left)
    sort(right)
    i = 0
    for k in left + middle + right:
        x[i] = k
        i += 1


sort(x)
for k in range(len(x)):
    print(chr(x[k]), end='')
print('.')
