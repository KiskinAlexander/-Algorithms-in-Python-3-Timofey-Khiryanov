# Решите задачу о количестве способов достичь точки n из точки 1, если кузнечик умеет прыгать +1, +2 и *3.
def grass_mov(N):
    K = [0, 1, 2, 4] + [0] * (N-3)
    for i in range(4, N + 1):
        if i % 3 == 0:
            K[i] = K[int(i / 3)] + K[i - 2] + K[i - 1]
        else:
            K[i] = K[i - 2] + K[i - 1]
    return K


f = int(input('Введите n:'))
print(grass_mov(f))
