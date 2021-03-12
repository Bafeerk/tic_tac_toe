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
    field[row][column] = 'X'
    draw_field(field)
