import grid
import minmax

# не понятно за что отвечает g, пожно переименовать в game_grid
# лучше указать так же тип переменной, потому что это класс, чтобы было понятно откуда методы вообще эти


def computer_step(g):
    n = g.n
    # i, j разумнее называть осмысленно. Можно не row, а row_id, например ещёы
    for row in range(n):

        for column in range(n):
            if g.get(row, column) == grid.CELL_EMPTY:
                g.set(row, column, grid.CELL_COMPUTER)

                # result не совсем корректное название. Флаги лучше называть в формате is_действие или is_not действие

                is_won = minmax.player_wins(g)
                if not is_won:
                    return

                g.set(row, column, grid.CELL_EMPTY)

    for row in range(n):
        for column in range(n):
            if g.get(row, column) == grid.CELL_EMPTY:
                g.set(row, column, grid.CELL_COMPUTER)
                return


# не понятно за что отвечает g, пожно переименовать в game_grid
# лучше указать так же тип переменной, потому что это класс, чтобы было понятно откуда методы вообще эти


def player_step(g):
    print(g.draw())
    while True:
        # Лучше назвать переменные осознанными названиями.
        row, column = list(map(int, input("Enter row and column: ").split(" ")))
        row, column = row - 1, column - 1
        if g.valid_coords(row, column) and g.get(row, column) == grid.CELL_EMPTY:
            g.set(row, column, grid.CELL_PLAYER)
            #
            break
        else:
            print("Invalid coordinates!")


def main():
    n = int(input("Enter grid size: "))

    # не понятно за что отвечает g, пожно переименовать в game_grid
    # лучше указать так же тип переменной, потому что это класс, чтобы было понятно откуда методы вообще эти

    g = grid.Grid(n)
    empty_cells = n * n

    # Триггерит с while True, можно убрать
    while True:
        computer_step(g)
        # все return'ы ниже можно убрать, если продумать завршение программы.
        if g.who_won() == grid.COMPUTER_WON:
            print("Computer won!")
            return
        empty_cells -= 1
        if empty_cells == 0:
            print("Neither won!")
            return
        player_step(g)
        if g.who_won() == grid.PLAYER_WON:
            print("Player won!")
            return

        # Дублирование кода выше, думаю, что нужно поправить
        empty_cells -= 1
        if empty_cells == 0:
            print("Neither won!")
            return


if __name__ == "__main__":
    main()
