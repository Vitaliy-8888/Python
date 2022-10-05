# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16]; 	
# - [2, 3, 5, 6] => [12, 15]

# Задайте список из n случайных чисел
# from random import random


def get_list(n):
    list_random = []
    for i in range(1, n + 1):
        list_random.append(random.randint(0, 9))
    return list_random


# нахождение произведений пар чисел списка
def pair_miltipiy(list_random):
    list_miltipiy = []
    for i in range(0, len(list_random) // 2):   # - находим длину списка и проходим половину списка 
        # перемножаем элементы сначала и с конца списка и добавляем в новый список:
        list_miltipiy.append(list_random[i] * list_random[-i-1])
    
    #  если количество элментов списка нечетное, то добавляем средний элемент списка возведенный в квадрат
    if len(list_random) % 2:
        # if len(list_random) % 2 == 1   # другой вриант проверки на нечетность
        list_miltipiy.append(list_random[(len(list_random) // 2)] ** 2)
    return list_miltipiy





# # Марат начал задаччу, но потом перебили
# list1 = [2, 3, 5, 6]
# for i in range(len(list1)/2):     # - находим длину списка и проходим половину списка     


# a = 5
# b = 3
# c = a + b
# print(c)

