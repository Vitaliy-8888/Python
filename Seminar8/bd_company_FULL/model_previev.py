# - показать всю базу

import model_creation   # импортируем данные из файла "model_creation.py"


def previev_base():        # - показать всю базу
    # SELECT * FROM personal - ВЫБРАТЬ * (все колонки) ИЗ БД personal
    for i in model_creation.cursor.execute('SELECT * FROM personal'):
        print(*i)				# печатаем все колонки из базы
        # print(f'номер = {i[0]}, имя = {i[1]}, фамилия = {i[2]}, должность = {i[3]}, зарплата = {i[4]}, премия = {i[5]}')



