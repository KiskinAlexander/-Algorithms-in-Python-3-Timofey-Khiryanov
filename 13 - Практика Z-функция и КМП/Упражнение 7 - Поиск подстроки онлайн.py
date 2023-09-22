# лень

def p_func(s):
    v = [0] * len(s)
    for i in range(1, len(s)):
        k = v[i - 1]
        while k > 0 and s[k] != s[i]:
            k = v[k - 1]
        if s[k] == s[i]:
            k = k + 1
        v[i] = k
    return v


s1 = input()
s2 = input()

n = len(s1)
m = len(s2)
pf = p_func(s2 + '#' + s1)
s = []
for i in range(m, n + 4):
    if pf[i] == m:
        s.append(i - m - 2)
print(*s)
