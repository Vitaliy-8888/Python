# Выборка по зарплате

import model_creation   # импортируем данные из файла "model_creation.py"


def more_salary():      # Посмотреть сотрудников, у кого зарплата выше указанной суммы
    sal = int(input("Введите сумму: "))
    # обращаемся к файлу "model_creation.py"
    model_creation.cursor.execute("""SELECT * FROM PERSONAL WHERE salary >= ?""", (sal,))
    for one in model_creation.cursor.fetchall():
        print(f'ID = {one[0]}, Имя = {one[1]}, Фамилия = {one[2]}, Должность = {one[3]}, Зарплата = {one[4]}, Бонусы = {one[5]}')
        # one = model_creation.cursor.fetchall()
        # print(*one)
    # one = model_creation.cursor.fetchall()
    # print(*one)