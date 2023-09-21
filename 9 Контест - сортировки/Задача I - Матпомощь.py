# Студентов надо построить в шеренгу от самого легкого до самого тяжелого.
# Кто мало весит - тем выдать матпомощь.
# При одинаковом весе сначала идет студент с большим ростом (тощий).
# Ввод: 3\n1.8 70\n1.75 70\n1.8 69.5 Вывод: 1.80 69.500\n1.80 70.000\n1.75 70.000
def point(str1, n):
    str2 = ''
    str3 = ''
    j = 0
    if '.' in str1:
        for i in range(len(str1)):
            if str1[i] == '.':
                while i + j + 1 != len(str1):
                    j += 1
                str2 = str1[i + j::].ljust(n - j + 1, '0')
            str3 = str1[:i] + str2
    else:
        str3 = str1 + '.' + '0' * n
    return str3


n = int(input())
C = []
for i in range(n):
    A = input().split(' ')
    C.append(A)

C1 = sorted(C, key=lambda x: float(x[0]), reverse=True)
C2 = sorted(C1, key=lambda x: float(x[1]))

for i in range(len(C2)):
    print(point(C2[i][0], 2), point(C2[i][1], 3))
