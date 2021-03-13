def draw_field(field):
    """
        Функция рисует поле
        Принимает список, ничего не возвращает
    """
    i = 0
    while i < len(field):
        print(field[i])
        i = i + 1

def coordinate_request(string):
    """
        Проверяет, что игрок ввел знчение от 1 до 3
        Принимает строку
        Возвращает int от 1 до 3
    """
    while True:
        x = input(string)
        if x in ['1', '2', '3']:
            x = int(x)
            return x
        else:
            print('Введите число от 1 до 3')
            continue

def check_rows(field, symbol):
    """
        Проверяет ряды массива на наличие трех идущих подряд 'X' или '0'
        Принимает массив и строку ('X' или 'Y')
        Возвращает bool
    """
    if field[1][1] + field[1][2] + field[1][3] == symbol * 3:
        print('check_rows, 1')
        return True
    elif field[2][1] + field[2][2] + field[2][3] == symbol * 3:
        return True
    elif field[3][1] + field[3][2] + field[3][3] == symbol * 3:
        return True
    else:
        return False

def check_columns(field, symbol):
    """
        Проверяет столбцы массива на наличие трех идущих подряд 'X' или '0'
        Принимает массив и строку ('X' или 'Y')
        Возвращает bool
    """
    if field[1][1] + field[2][1] + field[3][1] == symbol * 3:
        print('check_columns, 1')
        return True
    elif field[1][2] + field[2][2] + field[3][2] == symbol * 3:
        return True
    elif field[1][3] + field[2][3] + field[3][3] == symbol * 3:
        return True
    else:
        return False

def check_diagonals(field, symbol):
    """
        Проверяет диагонали массива на наличие трех идущих подряд 'X' или '0'
        Принимает массив и строку ('X' или 'Y')
        Возвращает bool
    """    
    if field[1][1] + field[2][2] + field[3][3] == symbol * 3:
        return True
    elif field[3][1] + field[2][2] + field[1][3] == symbol * 3:
        return True
    else:
        return False

def is_win(field, symbol):
    """
        Проверяет поле на наличие трех идущих подряд 'X' или '0'
        Получает массив поля, и строку ('X' или 'Y')
        Возвращает bool
    """
    if check_rows(field, symbol):
        return True
    elif check_columns(field, symbol):
        return True
    elif check_diagonals(field, symbol):
        return True
    else:
        return False

def computer(field):
    """
        Имитирует ход компьютера, ставит '0' на свободное место '-'
        Принимает массив
        Ничего не возвращает
    """
    pass
    
field = [
         [0, '1', '2', '3'],
         [1, '-', '-', '-'],
         [2, '-', '-', '-'],
         [3, '-', '-', '-']
        ]

draw_field(field)

while True:
    row = coordinate_request('Ряд: ')
    column = coordinate_request('Столбец: ')

    if field[row][column] != '-':
        draw_field(field)
        print('Поле занято')
        continue
    
    field[row][column] = 'X'

    if is_win(field, 'X'):
        draw_field(field)
        print('Поздравляем, вы выиграли')
        break

    draw_field(field)

    computer(field)

    if is_win(field, 'Y'):
        draw_field(field)
        print('Поздравляем, вы проиграли')
        break
    
    draw_field(field)
