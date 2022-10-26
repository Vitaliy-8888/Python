# - показать всю базу

import model_creation   


def previev_base():      
    # SELECT * FROM personal - ВЫБРАТЬ * (все колонки) ИЗ БД personal
    for i in model_creation.cursor.execute('SELECT * FROM personal'):
        print(*i)				
       


