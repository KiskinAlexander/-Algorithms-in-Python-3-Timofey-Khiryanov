# Напечатайте входную последовательность натуральных чисел, отсортировав ее по возрастанию сначала единиц,
# потом десятков, потом сотен и тп.
# Ввод: 5\n 5 23 3 43 123 Вывод: 3 23 123 43 5
n = int(input())
print(*sorted(input().split(), key=lambda x: x[::-1]))
