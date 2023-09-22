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
n = len(s1)
m = [0] * (n + 1)
answer = 0
for i in range(0, n):
    z = p_func(s1 + str(i))
    answer += n - i - m[i]
    for j in range(i + 1, n):
        m[j] = max(m[j], z[j - i])
print(answer)
