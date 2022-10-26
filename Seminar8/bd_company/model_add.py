# добавляем нового сотрудника в базу

import model_creation   


def add_record():               
    number_id = int(input("Введите номер сотрудника: "))
    nam = input("Введите имя: ")
    last_nam = input("Введите фамилию: ")
    pos = input("Введите должность: ")
    sal = int(input("Введите размер зарплаты: "))
    bon = int(input("Введите размер премии: "))
    
    try:            # запишем и сохраним значения в БД
        # cursor.execute - занесет в базу только одно значение  
        # INSERT INTO personal VALUES - ВСТАВИТЬ В БД personal ЗНАЧЕНИЯ (?,?,?,?,?,? – колонки БД)
        model_creation.cursor.execute('INSERT INTO personal VALUES(?,?,?,?,?,?)',
        (number_id, nam, last_nam, pos, sal, bon,))       # заносим в базу данные, введенные пользователем
        model_creation.bd.commit()                      # bd.commit() - сохранение БД
        print("Запись добавлена")
    except:            # except - функция исключит, те значения, которые уже сеть в БД
        print('Данные уже есть')

