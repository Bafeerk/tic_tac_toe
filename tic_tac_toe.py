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
        Проверяет ряды массива на наличие трех идущих подряд 'X' или 'O'
        Принимает массив и строку ('X' или 'O')
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
        Проверяет столбцы массива на наличие трех идущих подряд 'X' или 'O'
        Принимает массив и строку ('X' или 'O')
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
        Проверяет диагонали массива на наличие трех идущих подряд 'X' или 'O'
        Принимает массив и строку ('X' или 'O')
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
        Проверяет поле на наличие трех идущих подряд 'X' или 'O'
        Получает массив поля, и строку ('X' или 'O')
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

def computer_cheks_rows(field):
    """
        Проверяет строки на наличие в низ двух 'XX' и '-'
        Принимает массив
        Возвращает bool
    """
    print('I checks rows')
    i = 1
    while i < 4:
        if field[i][1] + field[i][2] + field[i][3] == '-XX':
            print('computer checks, 1')
            field[i][1] = 'O'
            return True
        elif field[i][1] + field[i][2] + field[i][3] == 'X-X':
            field[i][2] = 'O'
            return True
        elif field[i][1] + field[i][2] + field[i][3] == 'XX-':
            field[i][3] = 'O'
            return True
        i += 1
    return False

def computer_cheks_columns(field):
    """
        Проверяет столбцы на наличие в низ двух 'XX' и '-'
        Принимает массив
        Возвращает bool
    """
    print('Hi, I checks columns')
    i = 1
    while i < 4:
        if field[1][i] + field[2][i] + field[3][i] == '-XX':
            print('computer checks, 1')
            field[1][i] = 'O'
            return True
        elif field[1][i] + field[2][i] + field[3][i] == 'X-X':
            field[2][i] = 'O'
            return True
        elif field[1][i] + field[2][i] + field[3][i] == 'XX-':
            field[3][i] = 'O'
            return True
        i += 1
    return False

def computer(field):
    """
        Имитирует ход компьютера, ставит 'O' на свободное место '-'
        Принимает массив
        Ничего не возвращает
    """
    if computer_cheks_rows(field): 
##        computer_cheks_rows(field)
        pass
    elif computer_cheks_columns(field):
        pass
    else:        
        if  column + 1 < 3:
            if field[row][column + 1] == '-':
                field[row][column + 1] = 'O'
            else:
                if row + 1 < 3:    
                    field[row + 1][column] = 'O'
                else:
                    print('Я не знаю куда ходить')
        else:
            field[row + 1][column] = 'O'
    
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

    if is_win(field, 'O'):
        draw_field(field)
        print('Поздравляем, вы проиграли')
        break
    
    draw_field(field)
