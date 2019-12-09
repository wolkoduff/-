vector = int(input())
a = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0,' '0', '0', '0', '0', '0', '0']
global j
new_vector = ""
j = 0

print("Начальный вектор: ", a)
for i in range(1, len(a) - 1, 1):
    j += 1
    if a[i - 1] == '0' and a[i] == '0' and a[i + 1] == '0':
        print("Шаг №", j, ". Новый вектор:", new_vector)
    else:
        print("Шаг №", j, ". Новый вектор: ", new_vector)

print("Результат:", new_vector)
