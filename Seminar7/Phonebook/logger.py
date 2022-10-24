from spisok import get_abonent          # из файла spisok.py импоритруем функцию get_abonent
abonent = get_abonent()                 



def format_txt():
    with open ('log.txt', 'a', encoding = 'utf-8') as file:      # записываем данные в файл 'log.txt':
        file.write(f'Фамилия: {abonent[0]}\nИмя: {abonent[1]}\nТелефон: {abonent[2]}\nОписание: {abonent[3]}\n\n')



def format_scv():
    with open ('log.csv', 'a', encoding = 'utf-8') as file:     # записываем данные в файл 'log.csv':
        file.write(f'{abonent[0]}, {abonent[1]}, {abonent[2]}, {abonent[3]}\n\n')


