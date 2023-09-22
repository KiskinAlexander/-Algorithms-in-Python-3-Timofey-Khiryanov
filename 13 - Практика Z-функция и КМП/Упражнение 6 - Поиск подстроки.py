def prefix(s):
    v = [0] * len(s)
    for i in range(1, len(s)):
        k = v[i - 1]
        while k > 0 and s[k] != s[i]:
            k = v[k - 1]
        if s[k] == s[i]:
            k = k + 1
        v[i] = k
    return v


def kmp(Text, Sub: str):
    k = 0
    A = []
    pi = prefix(Sub)
    for i in range(0, len(Text)):
        while k > 0 and Text[i] != Sub[k]:
            k = pi[k - 1]
        if Text[i] == Sub[k]:
            k = k + 1
        if k == len(Sub):
            A.append(i)
            k = pi[k - 1]
    return A


text = input('Текст: ')
sub = input('фрагмент для поиска в тексте: ')

zf = print(kmp(text, sub))
