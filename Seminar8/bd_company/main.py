# Задача 8_1. Доделать решение задачи: Задача: Создать информационную систему 
# позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы

# главное меню базы данных


from model_add import add_record
from model_previev import previev_base
from model_find import find_record
from model_change import change_record
from modеl_delete import delete_record   


def input_choice():
    while True:
        user_choice = int(input('''
1 - показать всю базу
2 - добавить запись
3 - найти запись
4 - изменть запись
5 - удалить запись 
6 - выход
Введите вариант работы с базой: '''))

        if user_choice == 1:
            previev_base()
        elif user_choice == 2:
            add_record()
        elif user_choice == 3:
            find_record()
        elif user_choice == 4:
            change_record()
        elif user_choice == 5:
            delete_record()
        elif user_choice == 6:
            print('Выход')
            break
        else:
            print('Нет такого варианта')


input_choice()

