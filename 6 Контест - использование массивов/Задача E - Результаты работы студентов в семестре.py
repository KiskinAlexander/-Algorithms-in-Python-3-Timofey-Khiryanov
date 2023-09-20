# Есть результаты работы студентов в семестре. Студентов выводить в порядке суммы их баллов.
# Требутеся вывести отсортированные результаты работ для каждого студента.
# Данные вводятся как: student_id value
# student_id принимает значения от 0 до N. value от 1 до 10
# Пример входных данных: 2\n0 3\n0 5\n1 3\n1 2\n#
# Тут представленны данные о двух студента: 0 и 1. Сумма балов студента 0 - 8. Студента 1 - 5.
# Значит, сначала должны быть напечатаны результаты 0 студента, затем 1.
# Таким образом сначала надо вывести отсортированные результаты студента 0, затем студента 1:
# 5 3 3 2
student_count = int(input())
results = input()
std_input = []
students_lst = []
while results != '#':
    std_input.append(results)
    results = input()
for i in range(student_count):
    tmp_lst = []
    for t in range(len(std_input)):
        tmp = std_input[t].split()
        if int(tmp[0]) == i:
            tmp_lst.append(int(tmp[1]))
    if tmp_lst:
        students_lst.append(tmp_lst)
students_lst.sort(key=lambda s: (sum(s), s.sort(reverse=True)), reverse=True)
for i in students_lst:
    for t in i:
        print(t, end=' ')
