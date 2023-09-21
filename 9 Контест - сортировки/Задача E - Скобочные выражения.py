# Некоторые скобочные структуры правильные, другие — неправильные. Ваша задача — определить правильная ли
# скобочная структура.
# Ввод: () Вывод: YES
# Ввод: )( Вывод: NO
def check(s):
    count_0 = 0
    count_1 = 0
    for i in range(len(s)):
        if s[i] == '(':
            count_1 += 1
        elif s[i] == ')' and count_1 > count_0:
            count_0 += 1
        else:
            return 'NO'
    if count_0 == count_1:
        return 'YES'
    return 'NO'


s1 = input()
print(check(s1))
