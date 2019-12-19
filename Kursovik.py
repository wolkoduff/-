print("Введите первое нечёткое число(тройку его параметров{a, x, b}, разделяя его пробелами: ")
a = input().split()
print("Введите второе нечёткое число(тройку его параметров{a, x, b}, разделяя его пробелами: ")
b = input().split()

A = []
B = []

A_new = []
B_new = []

maximum = 0.0
minimum = 9999.0
overloper = 0.0

for i in a:
    A.append(float(i))

for i in b:
    B.append(float(i))

for i in A:
    if i > maximum:
        maximum = i
    elif i < minimum:
        minimum = i
    else:
        overloper = i

A_new.append(minimum)
A_new.append(maximum)
A_new.append(overloper)

for i in B:
    if i > maximum:
        maximum = i
    elif i < minimum:
        minimum = i
    else:
        overloper = i

B_new.append(minimum)
B_new.append(maximum)
B_new.append(overloper)

C = [round(A_new[0] / B_new[0], 2), round((A_new[1] / B_new[1]), 2), round((A_new[2] / B_new[2]), 2)]
print("Первое нечёткое число(А):", A_new)
print("Второе нечёткое число(В):", B_new)
print("Деление нечётких чисел:", A_new, "/", B_new)
print("Ответ:", C)

