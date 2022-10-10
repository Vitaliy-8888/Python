# Задача 4_4. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

import random

k = int(input("Введите натуральную степень k: "))

spisok = {}         # создание списка: где ключи - это степень k, а значения - это рандомные коэффициенты многочлена

while k >= 0:                            # заполняем список
    koeff = random.randint(0, 100)      # задаем рандомные коэффициенты многочлена
    spisok[k] = koeff                   # добавляем коэффициенты многочлена в список
    k -= 1
print(f'Cписок степеней k и коэффициентов многочлена: {spisok}')


result = ''                         # изначально создаем пустую строку
for k in spisok:                    # проходимся по списку и собираем констркуцию многочлена
    if k == 0:                          
        result += f'{spisok[k]} = 0'    
    elif k == 1:                        
        result += f'{spisok[k]}x + '    
    else:                                   
        result += f'{spisok[k]}x^{k} + '    

print(f'Многочлен: {result}')


with open('file4_4.txt', 'w') as f:      # - создаем файл 'file4_4.txt'
    f.write(result)                     # - записываем в файл значение из result 
