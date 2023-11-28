# Статистика по минимальной, максимальной и средней зарплате

import model_creation   # импортируем данные из файла "model_creation.py"


def static_record():    # Статистика по зарплате
    # обращаемся к файлу "model_creation.py"
    model_creation.cursor.execute('SELECT count(*) as cnt, max(salary) as max_sal, min(salary) as min_sal, avg(salary) as avg_sal FROM PERSONAL;')
    for one in model_creation.cursor.fetchmany():
        print(f'''
        Количество сотрудников в базе = {one[0]}, 
        Максимальная зарплата = {one[1]}, 
        Минимальная зарплата = {one[2]}, 
        Средняя зарплата = {one[3]}''')