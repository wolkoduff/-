def movetower(count, fromtower, totower, withtower):
    if count >= 1:
        movetower(count - 1, fromtower, withtower, totower)
        movedisk(fromtower, totower)
        global i
        i += 1
        movetower(count - 1, withtower, totower, fromtower)


def movedisk(fp, tp):
    print("Номер хода:", i, "Передвигаем диск с", fp, "на", tp)


n = 3
i = 1
A = "Первый стержень"
B = "Второй стержень"
C = "Третий стержень"

movetower(n, A, B, C)
