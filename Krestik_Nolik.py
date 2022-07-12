print("Kрестики - нолики\n"
      "Это логическая игра для двух игроков на поле 3 на 3 клетки.")
# Для начала зададим поле. одномерный списком(list) с числами
# Создаём функцией range()
Pole = list(range(1, 10))


# Функция, для вывода поля
def console(Pole):
    print("-" * 13)  # Верхняя граница поля
    for i in range(3):
        print(f"| {Pole[0 + i * 3]} | {Pole[1 + i * 3]} | {Pole[2 + i * 3]} |")
        print("-" * 13)  # Нижни границы поля


# Условия победы
def win_Game(Pole):
    win_lin = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    # Кортеж (tuple) с выигрышными координатами
    for Cells in win_lin:
        if Pole[Cells[0]] == Pole[Cells[1]] == Pole[Cells[2]]:
            return Pole[Cells[0]]
    return False


# Ввод данных игроком
def ask(symbol):
    valid = False
    while not valid:
        number = input(f"Выбери место для {symbol} \n")
        try:
            number = int(number)
        except:
            print(f"Ошибка!!! Нажмите на цифру от 1 до 9?")
            continue
        # Проверка на наличие Х и О
        if 1 <= number <= 9:    # Ограничение выбора пользователя (от 1 до 9)
            if str(Pole[number - 1]) not in "XO":  #
                Pole[number - 1] = symbol
                valid = True
            else:
                print("Выберите другую клетку уже занята")
        else:
            print("Ошибка!!! Введите число от 1 до 9.")


def Game(Pole):
    counter = 0
    win = False
    while not win:
        console(Pole)
        if counter % 2 == 0:
            ask("X")
        else:
            ask("O")
        counter += 1
        if counter > 4:
            tmp = win_Game(Pole)
            if tmp:
                print(f'Победу одержал {tmp}')
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
        console(Pole)


Game(Pole)
