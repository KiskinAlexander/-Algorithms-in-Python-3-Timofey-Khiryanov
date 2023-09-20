# Определите тип треугольника (остроугольный, тупоугольный, прямоугольный) с данными сторонами.
# Ввод: 3\n4\n5 Вывод: right
a = int(input())
b = int(input())
c = int(input())

if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("right")
elif a >= b + c or b >= a + c or c >= a + b:
    print("impossible")
elif a**2 + b**2 >= c**2 and a**2 + c**2 >= b**2 and b**2 + c**2 >= a**2:
    print("acute")
else:
    print("obtuse")
