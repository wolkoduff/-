vector = input()
a = list(vector)
new_vector = ['0']
global j
j = 0
print("Начальный вектор: ", a)
for i in range(1, len(a) - 1, 1):
    j += 1
    if a[i - 1] == '0' and a[i] == '0' and a[i + 1] == '0':
        new_vector.append('1')
        print("Шаг №", j, ". Новый вектор:", new_vector)
    else:
        new_vector.append('0')
        print("Шаг №", j, ". Новый вектор: ", new_vector)

new_vector.append('0')
print(len(a))
print(len(a)-1)
print(len(new_vector))
print("\nНачальный вектор: ", a)
print("Результат:", new_vector)
