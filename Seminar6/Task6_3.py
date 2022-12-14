# Задача 6_3. Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# Вариант1 - Изначальный

spisok = [2, 3, 5, 9, 3]

def sum_odd_positions(spisok):
    summa = 0
    for i in range(len(spisok)):    # - проходим по всей длине списка
        if i % 2 != 0:              # - находим нечётные позиции (i) в списке
            summa += spisok[i]      # - складываем элементы [i] на нечётных позициях
    return print(f'Сумма элементов списка, стоящих на нечётных позициях = {summa}')


sum_odd_positions(spisok)



# Вариант 2 - предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

spisok = [2, 3, 5, 9, 3]     

result = [spisok[i] for i in range(len(spisok)) if i % 2 != 0]      
print(f'Сумма элементов списка, стоящих на нечётных позициях = {sum(result)}')
