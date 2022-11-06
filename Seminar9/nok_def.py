# 3 Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

# a = int(input("Введите число a:"))
# b = int(input("Введите число b:"))
#
def nod(a, b):
    if b == 0:
        return a
    else:
        return nod(b, a % b)


def nok(a, b):
    return int(abs((a * b)) / nod(a, b))


# print(nod(a,b))
# print(nok(a,b))