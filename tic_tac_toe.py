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
def is_win(field):
    """
        Проверяет поле на наличие трех идущих подряд 'X' или '0'
        Получает массив поля
        Возвращает bool
    """
    pass
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
    if is_win(field):
        draw_field(field)
        print('Поздравляем, вы выиграли')
        break
    field[row][column] = 'X'
    draw_field(field)

    computer(field)

    if is_win(field):
        draw_field(field)
        print('Поздравляем, вы выиграли')
        break
    
    draw_field(field)
