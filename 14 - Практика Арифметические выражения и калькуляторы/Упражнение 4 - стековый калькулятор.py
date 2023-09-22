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


s = [2,3,'-',12,10,'-','*',1334,2,'/','+']

for i in range(len(s)):
    if str(s[i]).isdigit():
        push(s[i])
    else:
        y = int(pop())
        x = int(pop())
        if s[i] == '+':
            z = x + y
        elif s[i] == '-':
            z = x - y
        elif s[i] == '*':
            z = x * y
        elif s[i] == '/':
            z = x / y

        push(z)
if len(_stack) == 1:
    print(pop())

        
       
