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


def conv(expr):
    prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    pl = []
    tl = expr
    for t in tl:
        if t.isdigit():
            pl.append(t)
        elif t == '(':
            push(t)
        elif t == ')':
            top = pop()
            while top != '(':
                pl.append(top)
                top = pop()
        else:
            while (not is_empty()) and (prec[_stack[-1]]-1 >= prec[t]):
                pl.append(pop())
            push(t)
    while not is_empty():
        pl.append(pop())
    return " ".join(pl)
print(conv('(3+4*(2-1))/5'))