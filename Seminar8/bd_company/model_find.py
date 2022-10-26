# найти запись в базе 

import model_creation   


def find_record():        
    last_nam = input('Введите фамилию: ')
    # выбрать все колонки из базы personal где фамилия будет как введенный last_nam  
    model_creation.cursor.execute(f'SELECT * FROM personal WHERE last_name LIKE "{last_nam}"')
    one = model_creation.cursor.fetchall()            #   fetchall - извлечь всех
    if one != []:       # если в результате запроса есть значения, тогда:  
        for i in one:
            print(*i)           
    else:   
        print(f"В базе нет сотрудника c фамилией {last_nam}")

