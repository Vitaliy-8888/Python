# изменить запись в базе

import model_creation   # импортируем данные из файла "model_creation.py"
  

def change_record():
    number_id = int(input("Введите номер сотрудника: "))
    sal = int(input("Введите размер зарплаты: "))

    try:            # try - функция запишет и сохранит значения в БД
        # обращаемся к файлу "model_creation.py"
        # cursor.execute - занесет в базу только одно значение
        # поменять зарплату сотрудника:
        # UPDATE personal SET salary (ОБНОВИТЬ БД personal: УСТАНОВИТЬ з/п) = {sal} для id={number_id}
        model_creation.cursor.execute(f'UPDATE personal SET salary = {sal} WHERE id={number_id};')
        model_creation.bd.commit()               # bd.commit() - сохранение БД
        print("Данные по сотруднику изменены")
    except:            # except - функция исключит, те значения, которые уже сеть в БД
        print('Данные уже есть')    # !!!!- не работает, хотя раньше работало!!!!!



# # Вариант 2 - не работает, если нужно поменять несколько значений 
# # наверно нужно делать еще одно куруговое меню через графу column :
# # def find_record(column, nam):
# #     model_creation.cursor.execute(f'SELECT * FROM personal WHERE {column} LIKE {nam};')            

# def change_record():
#     number_id = int(input("Введите номер сотрудника: "))
#     last_nam = input("Введите фамилию: ")        # смена фамилии актуальна для женщин
#     pos = input("Введите должность: ")
#     sal = int(input("Введите размер зарплаты: "))
#     bon = int(input("Введите размер премии: "))

#     try:            # try - функция запишет и сохранит значения в БД
#         # обращаемся к файлу "model_creation.py"
#         # cursor.execute - занесет в базу только одно значение
#         # поменять данные сотрудника:
#         # UPDATE personal SET last_name (ОБНОВИТЬ БД personal: УСТАНОВИТЬ фамилию) = {last_nam} для id={number_id}
#         model_creation.cursor.execute(f'UPDATE personal SET last_name = {last_nam} WHERE id={number_id}')
#         # UPDATE personal SET position (ОБНОВИТЬ БД personal: УСТАНОВИТЬ должность) = {pos} для id={number_id}
#         model_creation.cursor.execute(f'UPDATE personal SET position = {pos} WHERE id={number_id}')
#         # UPDATE personal SET salary (ОБНОВИТЬ БД personal: УСТАНОВИТЬ з/п) = {sal} для id={number_id}
#         model_creation.cursor.execute(f'UPDATE personal SET salary = {sal} WHERE id={number_id}')
#         # UPDATE personal SET bonus (ОБНОВИТЬ БД personal: УСТАНОВИТЬ премию) = {bon} для id={number_id}
#         model_creation.cursor.execute(f'UPDATE personal SET bonus = {bon} WHERE id={number_id}')
#         model_creation.bd.commit()               # bd.commit() - сохранение БД
#         print("Данные по сотруднику изменены")
#     except:            # except - функция исключит, те значения, которые уже сеть в БД
#         print('Данные уже есть')
