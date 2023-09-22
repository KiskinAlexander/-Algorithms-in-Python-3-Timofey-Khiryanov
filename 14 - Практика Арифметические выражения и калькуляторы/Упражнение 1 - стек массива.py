# Напишите программу, которая последовательно кладет в стек произвольный массив чисел, а затем распечатывает их ,
# последовательно доставая, пока стек не пуст (например, набор (1,...,10)).
_stack = []


def push(x):
    _stack.append(x)


def pop():
    x = _stack.pop()
    return x


def clear():
    _stack.clear()


def is_empty():
    return len(_stack) == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(list1)):
    push(list1[i])
for i in range(len(list1)):
    print(pop(), end=" ")
