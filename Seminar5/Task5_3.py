# Задача 5_3. Создайте программу для игры в ""Крестики-нолики"".

# Вариант 5
# print(chr(11093)) # нолик
# print(chr(10060)) # крестик
# print(chr(127942)) # кубок
# print(chr(128075)) # приветствие

print(chr(128075), ' Давайте начнем игру!')

field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def draw_field(field):
    print('-------------')
    for i in range(3):
        print('|', field[0 + i * 3], '|',
              field[1 + i * 3], '|', field[2 + i * 3], '|')
        print('-------------')

# draw_field(field)


def move_in_game(player_move):
    value = False
    while not value:
        player_choice = input(f'Ход делает {player_move}: ')
        try:
            player_choice = int(player_choice)
        except:
            print('Вы ввели некорректное значение. Попробуйте еще раз.')
            continue
        if 9 >= player_choice >= 1:
            if (str(field[player_choice - 1]) not in ('XO')):
                field[player_choice - 1] = player_move
                value = True
            else:
                print(
                    'Невозможно выполнить ход в уже заполненную ячейку. Попробуйте еще раз.')
        else:
            print('Такой ячейки не существует. Попробуйте еще раз.')


def winning_positions(field):
    winning_coordinates = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                           (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for all in winning_coordinates:
        if field[all[0]] == field[all[1]] == field[all[2]]:
            return field[all[0]]
    return False


def game(field):
    count = 0
    victory = False
    while not victory:
        draw_field(field)
        if count % 2 == 0:
            move_in_game('X')
        else:
            move_in_game('O')
        count += 1
        if count > 4:
            temp = winning_positions(field)
            if temp:
                print(temp)
                print('Поздравляем! Победа! ', chr(127942))
                victory = True
                break
        if count == 9:
            print('Ничья!')
            break
    draw_field(field)


game(field)

file = open('Task5.3.txt', 'w', encoding='utf-8')
file.write(f'{field}\n')
file.close()
