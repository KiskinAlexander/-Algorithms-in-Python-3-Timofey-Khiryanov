# Числа трибоначчи - последовательность целых чисел {t n }, заданная с помощью рекуррентного соотношения:
# t 0 = 0, t 1 = 0, t 2 = 1 , t n+3 = t n + t n+1 + t n+2 Нужно найти номер первого числа трибоначчи,
# превосходящего заданное. Нумерация начинается с 0 .
# Ввод: 10 Вывод: 7

A = [0, 0, 1]
N = int(input())
i = 2
for j in range(N+1):
    A.append(A[j] + A[j+1] + A[j+2])
    
    if N < A[i]:
        break
    i += 1
print(i)
