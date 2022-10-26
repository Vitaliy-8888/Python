# создаем базу данных по компании 

import sqlite3    


bd = sqlite3.connect("Data_base.db")   # создаем базу данных (изначально пустую)

cursor = bd.cursor()        # выполнение SQL запросов


# CREATE TABLE IF NOT EXISTS personal (СОЗДАТЬ ТАБЛИЦУ personal, ЕСЛИ ОНА НЕ СУЩЕСТВУЕТ)
# id INTEGER PRIMARY KEY autoincrement  - создание уникальной автонумерации id
# создаваем колонки (id, Имя, фамилия, должность, зарплату, бонусы) в базе данных (БД)
cursor.execute('''CREATE TABLE IF NOT EXISTS personal(  
    id INTEGER PRIMARY KEY autoincrement,      
    name TEXT,
    last_name TEXT,
    position TEXT,
    salary INT,
    bonus INT
)''')
