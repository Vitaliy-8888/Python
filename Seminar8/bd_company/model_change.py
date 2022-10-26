# изменить запись в базе

import model_creation   
  

def change_record():
    number_id = int(input("Введите номер сотрудника: "))
    sal = int(input("Введите размер зарплаты: "))

    try:             # запишем и сохраним значения в БД
        # UPDATE personal SET salary (ОБНОВИТЬ БД personal: УСТАНОВИТЬ з/п) = {sal} для id={number_id}
        model_creation.cursor.execute(f'UPDATE personal SET salary = {sal} WHERE id={number_id};')
        model_creation.bd.commit()               # bd.commit() - сохранение БД
        print("Данные по сотруднику изменены")
    except:           
        print('Данные уже есть')   

