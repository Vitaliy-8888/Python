# Задача 9_1. Создайте программу для игры в ""Крестики-нолики"" 
# при помощи виртуального окружения и PIP


from tictactoe import Board


def program(board):

    i = 0
    print(board)                    # печать поля игры
    print(f'Игру начинают крестики\n')
    while i <= 9:
        try:            # ввод координат поля 
            x = int(input('Введите координату от 0 до 2 для X = '))
            y = int(input('Введите координату от 0 до 2 для Y = '))

            if board.is_empty((x, y)):
                board.push((x, y))
                if board.result() == 1:     # Выиграли крестики
                    print(f"\nПобедили крестики!!!")
                    print(board)
                    break
                elif board.result() == 2:    # Выиграли нолики
                    print(f"\nПобедили нолики!!!")
                    print(board)
                    break
            else:
                print("Это поле уже занято")
                i -= 1
            i += 1
            if i == 9:   # если все поля заполнены
                print(f"\nНИЧЬЯ!!!")
                print(board)
                break
            print(board)
        except:
            print("координата должна быть от 0 до 2")


program(Board((3, 3), 3))