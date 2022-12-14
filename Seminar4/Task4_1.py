# Задача 4_1. Вычислить число c заданной точностью d
        # Пример:
        # при d = 0.001, π = 3.141        10-1 <= d <= 10-10


import math

d = input('Введите число d: ')      # число d приходит в виде строки

if ('.') in d:                   	# если находим точку в числе d
    result = d.split('.')  		    # split -  делим число d по точке и получаем целую и дробные части
    result = len(result[1])         # находим длину дробной части числа d
elif (',') in d:                 	
    result = d.split(',') 	          
    result = len(result[1])        
else:
    result = 0

print(f'Число c заданной точностью d = {round(math.pi, result)}')  # число π округляем до знака как у числа d
