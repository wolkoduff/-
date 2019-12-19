print("Введите первое нечёткое число(тройку его параметров{a, x, b}, где a <= x, b <= x, x - точка максимума графика функции), разделяя его пробелами: ")
a = input().split()
print("Введите второе нечёткое число(тройку его параметров{a, x, b}, где a <= x, b <= x, x - точка максимума графика функции), разделяя его пробелами: ")
b = input().split()

print("Введите первое нечёткое число(тройку его параметров{a, x, b}), разделяя его пробелами: ")
a = input().split()
print("Введите второе нечёткое число(тройку его параметров{a, x, b}), разделяя его пробелами: ")
b = input().split()

A = []
B = []

for i in range(0, len(a), 1):
    if float(a[i]) != float(max(a)):
        A.append(float(a[i]))

kostil = A[1]
A[1] = float(max(a))
A.append(kostil)

for i in range(0, len(b), 1):
    if float(b[i]) != float(max(b)):
        B.append(float(b[i]))

kostil = B[1]
B[1] = float(max(b))
B.append(kostil)

C = [round(B[0] / A[2], 2), round((A[1] / B[1]), 2), round((B[2] / A[0]), 2)]
print("Первое нечёткое число(А):", A)
print("Второе нечёткое число(В):", B)
print("Деление нечётких чисел:", A, "/", B)
print("Ответ:", C)
