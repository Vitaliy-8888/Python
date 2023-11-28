# создаем базу данных по компании (изначально пустую)

import sqlite3    # импортируем базу данных


bd = sqlite3.connect("Data_base.db")   # создаем базу данных (БД): с названием bd в файле "Data_base.db"

cursor = bd.cursor()        # нужно объявить курсор, который будет выполнять SQL запросы

# будем создавать, колонки (id, Имя, фамилия, должность, зарплату, бонусы) в нашей базе данных (БД)
# поставим условие, если существует БД, что бы не создавать БД 2-й раз:
# CREATE TABLE IF NOT EXISTS personal (СОЗДАТЬ ТАБЛИЦУ personal, ЕСЛИ ОНА НЕ СУЩЕСТВУЕТ)
# id INTEGER PRIMARY KEY autoincrement  - создание уникальной автонумерации id
# или вместо "id INTEGER PRIMARY KEY autoincrement" можно просто написать "id INTEGER"
cursor.execute('''CREATE TABLE IF NOT EXISTS personal(  
    id INTEGER PRIMARY KEY autoincrement,      
    name TEXT,
    last_name TEXT,
    position TEXT,
    salary INT,
    bonus INT
)''')
