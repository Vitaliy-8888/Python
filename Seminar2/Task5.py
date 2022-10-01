# Задача 5. Реализовать алгоритм перемешивания списка.

import random    # - импортируем функцию random (генератор случайных чисел)

list_numbers = []     # - создаем пустой список

for i in range(0, 10):         
    list_numbers.append(random.randint(1, 100))  # - добавляем в список list_numbers случайные числа (1-99)

print(f'Изначальный список чисел {list_numbers}')

result = []        
result1 = []        
for i in list_numbers:  
    if i % 2 == 0:      
        result.append(i)   # - добавляем четные элементы в список result
    else:
        result1.append(i)  # - добавляем НЕ четные элементы в список result1

result.sort()        # - функция sort сортирует числа по возрастанию в списке 
result1.sort()       
        
result.extend(result1)  # - метод extend добавляет в конец списка result список result1
print(f'Перемешанный спиcок чисел {result}')

