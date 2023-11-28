# добавляем нового сотрудника в базу

import model_creation   # импортируем данные из файла "model_creation.py"


def add_record():               # пользователь вводит данные по сотруднику
    number_id = int(input("Введите номер сотрудника: "))
    nam = input("Введите имя: ")
    last_nam = input("Введите фамилию: ")
    pos = input("Введите должность: ")
    sal = int(input("Введите размер зарплаты: "))
    bon = int(input("Введите размер премии: "))
    
    try:            # try - функция запишет и сохранит значения в БД
        # обращаемся к файлу "model_creation.py"
        # cursor.execute - занесет в базу только одно значение  
        # cursor.executemany - занесет в базу сразу все значения 
        # INSERT INTO personal VALUES - ВСТАВИТЬ В БД personal ЗНАЧЕНИЯ (?,?,?,?,?,? – колонки БД)
        model_creation.cursor.execute('INSERT INTO personal VALUES(?,?,?,?,?,?)',
        (number_id, nam, last_nam, pos, sal, bon,))       # заносим в базу данные введенные пользователем
        model_creation.bd.commit()                      # bd.commit() - сохранение БД
        print("Запись добавлена")
    except:            # except - функция исключит, те значения, которые уже сеть в БД
        print('Данные уже есть')

