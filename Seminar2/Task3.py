# Задача 3. Задать список из n чисел последовательности (1 + 1/n)^n    
# и вывести на экран их сумму.
# Пример - Для n = 6:
# [2.0, 2.25, 2.3704, 2.4414, 2.4883, 2.5216]
# Сумма чисел = 14.0717

number = int(input("Введите число n: "))  

sequence = []   # - задаем новый список        
for i in range(1, number+1):   # - перебираем все элементы списка
    result = (1 + 1/i)**i    
    sequence.append(round(result, 4))   # добавляем в конец списка sequence элемент result с округлением

print(sequence)   
print(f'Сумма чисел = {sum(sequence)}')  