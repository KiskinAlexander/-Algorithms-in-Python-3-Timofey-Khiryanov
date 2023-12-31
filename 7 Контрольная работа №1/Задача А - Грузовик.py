# Вы - водитель грузовика с открытым кузовом. В кузове два груза: пианино и холодильник. Пианино необходимо доставить
# в институт, холодильник в общежитие. В каждое из этих мест ведет отдельная дорога, начинающаяся от перекрестка,
# на котором Вы стоите, других дорог в мире нет. Известно, что по дороге в институт есть мост, на котором действует
# ограничение максимальной допустимой массы автомобиля с грузом, а по дороге в общежитие есть туннель с ограничением
# высоты. Требуется определить, возможно ли доставить грузы или нет(разумеется, сгружать их, где попало, Вам запрещено).
# На вход подается 8 чисел натуральных чисел (каждое < 100), каждое в новой строке, в следующем порядке: вес грузовика
# без груза, высота платформы кузова (на которой стоят грузы), вес пианино, высота пианино, вес холодильника, высота
# холодильника, максимальный допустимый вес на мосту, максимальная допустимая высота в туннеле
# Примечание: пианино и холодильник заведомо возвышаются над кабиной грузовика, т.е. высоту кабины можно в расчет
# не принимать.
# Вывести YES если доставка возможна и NO в противном случае.
A = []
for i in range(0, 8):
    A.append(int(input()))
print("YES" if (A[0] + A[2] <= A[6] and A[1] + A[5] <= A[7]) and
        ((A[0] + A[2] + A[4] <= A[6]) or (max(A[3], A[5])+A[1] <= A[7])) else "NO")
