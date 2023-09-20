# Пусть задана строка s. Назовем ее k-ой (k > 0) степенью s^k строку s^k = sss (k раз).
# Например, третьей степенью строки abc является строка аbсаbсаbс.
# Корнем k степени из строки s называется такая строка t (если она существует), что t^k = s.
# Ваша задача состоит в том, чтобы написать программу, находящую степень строки или корень из нее.
# На вход программе подается 2 строки. Первая содержит строку S, вторая - степень k.
# Отрицательная степень означает взятие корня соответствующей степени.
# Ввод: abcdabcd\n-2 Вывод: abcd
# Ввод: abcd\n-4 Вывод: NO SOLUTION
# Ввод: abc\n3 Вывод: abcabcabc
def str_sqrt(s: str, k: int):
    flag = True
    if len(s) % k != 0:
        return "NO SOLUTION"
    k = -k
    size = len(s) // k
    new_str = s[:size]

    for i in range(1, k):
        for j in range(size):
            flag = (new_str[j] == s[j + size * i]) and flag
    return new_str if flag else "NO SOLUTION"


s = input()
k = int(input())

if k >= 0:
    print(s * k)
else:
    print(str_sqrt(s, k))
