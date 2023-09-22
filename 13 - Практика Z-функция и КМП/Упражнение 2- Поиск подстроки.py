def z_func(s):
    z = [0] * len(s)
    l, r = 0, 0
    for i in range(1, len(s)):
        z[i] = max(0, min(z[i - l], r - i))
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z


s1 = input("Введите полную строку:")
s2 = input("Введите подстроку для поиска в исходной:")
n = len(s1)
m = len(s2)
zf = z_func(s2 + '#' + s1)
s = []
for i in range(m, n + 2):
    if zf[i] == m:
        s.append(i - m)
print(*s)
