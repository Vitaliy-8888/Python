# Задача 5. Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи] (https://ru.wikipedia.org/wiki/Негафибоначчи)


def fib(n):     # функция для Фибоначчи
    # прописали логику выхода из функции: 
    if n == 1:       
        return 0   
    elif n == 2:    
        return 1    
    return fib(n-1) + fib(n-2) # Иначе возвращаем рекурсивный вызов для n-1 и n-2


def nega_fib(n):            # функция для Негафибоначчи
    negafibonacci = []		# создали новый список для Негафибоначчи
    for i in range(1, n + 1):		# проходимся по списку
        negafibonacci.append(fib(i))   # считаем Фибоначчи и добавляем в конец списка 
        if i != 1:      
            negafibonacci.insert(0, (-1) ** (i) * fib(i)) # считаем Негафибоначчи и добавляем в начало списка 
    print(f'Список чисел Негафибоначчи: {negafibonacci}')
    

n = int(input('Введите число для списка Фибоначчи: '))
nega_fib(n)
