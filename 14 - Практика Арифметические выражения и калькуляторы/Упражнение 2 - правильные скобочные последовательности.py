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


def is_braces_sequence_correct(s: str):
    for brace in s:
        if brace not in "(){}<>":
            continue
        if brace in "({<":
            push(brace)
        else:
            if not is_empty():
                left = pop()
                right = ""
                if left == "(":
                    right = ")"
                elif left == "{":
                    right = "}"
                elif left == "<":
                    right = ">"
                if brace == right:
                    continue
                return False
            return False
    return is_empty()

str1 = input('Введите строку для проверки(с использованием символов <>{}()):')
print(is_braces_sequence_correct(str1))
