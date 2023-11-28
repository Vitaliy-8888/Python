# найти запись в базе

import model_creation   # импортируем данные из файла "model_creation.py"

# Варианат 1 -  поиск по фамилии

def find_record():        # поиск по фамилии
    last_nam = input('Введите фамилию: ')
    # обращаемся к файлу "model_creation.py"
    # выбрать все колонки из базы personal где фамилия like (как) введенный last_nam  
    model_creation.cursor.execute(f'SELECT * FROM personal WHERE last_name LIKE "{last_nam}"')
    result = model_creation.cursor.fetchall()        #         fetchall - извлечь всех
    if result != []:     # если результат запроса оказался НЕ пустым (т.е. по выборке есть значения), тогда:  
        for i in result:
            print(*i)           # печатаем из базы все колонки по запросу 
    else:   # если результат запроса оказался пустым т.е. result == [] (по выборке нет значений), тогда 
        print(f"В базе нет сотрудника c фамилией {last_nam}")


# # Вариант 2 - поиск по ID 

# def find_record():            # поиск по ID - Вариант 2
#     number_id = int(input("Введите номер сотрудника: "))
#     # обращаемся к файлу "model_creation.py"
#     # выбрать все колонки из базы personal где id как (like) введенный number_id
#     model_creation.cursor.execute(f'SELECT * FROM personal WHERE id like {number_id};')
#     for one in model_creation.cursor.fetchall():        #         fetchall - извлечь всех
#         print(*one)
#         print(f'ID = {one[0]}, Имя = {one[1]}, Фамилия = {one[2]}, Должность = {one[3]}, Зарплата = {one[4]}, Бонусы = {one[5]}')
