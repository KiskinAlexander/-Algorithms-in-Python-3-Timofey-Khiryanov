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


s1 = input('Ведите строку:')
n = len(s1)
z = p_func(s1)
k = n - z[n - 1]
if n % (k) == 0:
    print(k, s1[:k])
else:
    print(n, s1[:n])
