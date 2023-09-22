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


def count1(s1):
    n = len(s1)
    m = [0] * (n + 1)
    answer = 0
    for i in range(0, n - 1):
        z = z_func(s1 + str(i))
        answer += n - i - m[i]
        for j in range(i + 1, n):
            m[j] = max(m[j], z[j - i])
    return answer


s1 = input()
print(count1(s1))
