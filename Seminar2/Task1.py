# Задача 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = input("Введите вещественное число: ")  

sum = 0
for i in number:  
    if i == '.':
        number = number.replace('.', '') 
    elif i == ',':
        number = number.replace(',', '')
    else:
        sum += int(i)   # int - переводим строку в число 

print(f'Сумма цифр в числе: {sum}')