# Задача 4. Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в списке positions - создайте этот список 
# (например: positions = [1, 3, 6]).

number = int(input("Введите число N: ")) 

position1 = int(input("Укажите позицию 1 элемента: ")) 
position2 = int(input("Укажите позицию 2 элемента: ")) 
position3 = int(input("Укажите позицию 3 элемента: ")) 

# - в функцию передаются значения:
# number - размер списка 
# position1, position2, position3 - позиции указанные пользователем
def list_numbers(number, position1, position2, position3):  
    res = []            # - задаем новый список 
    position  = [position1, position2, position3]   # - в список вносим позиции, которые ввел пользователь
    result = 1
    for i in range(-number, number+1):  # - создаем список [-N, N]
        res.append(i)   # - добавляем элементы в список

    for n in position:   # цикл по позициям
        result *= res[n]    
    return print(f'В списке {res}, произведение элементов на позициях {position1}, {position2}, {position3}, = {result}')
    
list_numbers(number, position1, position2, position3)
