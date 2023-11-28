# удаляем сотрудника из базы

import model_creation   # импортируем данные из файла "model_creation.py"

def delete_record():        # удалить запись
    number_id = int(input("Введите номер сотрудника: "))
    # обращаемся к файлу "model_creation.py"
    # - удаление записи с id = (номер id  по запросу)
    model_creation.cursor.execute(f'DELETE FROM personal WHERE id={number_id}') 
    model_creation.bd.commit()            # bd.commit() - сохранение БД
    print("Данные по сотруднику удалены")

