CELL_EMPTY = " "
CELL_PLAYER = "X"
CELL_COMPUTER = "O"

PLAYER_WON = -1
NEITHER_WON = 0
COMPUTER_WON = 1


class Grid:
    def __init__(self, n):
        self.n = n
        self.state = [CELL_EMPTY] * (n * n)

    def get(self, i, j):
        return self.state[self.n * i + j]

    def set(self, i, j, value):
        self.state[self.n * i + j] = value

    # i, j -> row, column
    def valid_coords(self, row, column):
        return (row >= 0 and row < self.n) and (column >= 0 and column < self.n)

    # не понятно из названий что такое di, dj, c
    def check(self, row, column, di, dj, c):
        required_to_win = min(5, self.n)
        count = 0
        # i, j -> row, column
        while (
            count < required_to_win
            and self.valid_coords(row, column)
            and self.get(row, column) == c
        ):
            count += 1
            row += di
            column += dj

        return count >= required_to_win

    def who_won(self):
        for row in range(self.n):
            for col in range(self.n):

                # Нет смысла ставить elif, если все условные операторы заканчиваются return'ом
                if self.check(row, col, +1, 0, CELL_PLAYER):
                    return PLAYER_WON

                if self.check(row, col, +1, 0, CELL_COMPUTER):
                    return COMPUTER_WON

                if self.check(row, col, 0, +1, CELL_PLAYER):
                    return PLAYER_WON

                if self.check(row, col, 0, +1, CELL_COMPUTER):
                    return COMPUTER_WON

                if self.check(row, col, +1, +1, CELL_PLAYER):
                    return PLAYER_WON

                if self.check(row, col, +1, +1, CELL_COMPUTER):
                    return COMPUTER_WON

                if self.check(row, col, +1, -1, CELL_PLAYER):
                    return PLAYER_WON

                if self.check(row, col, +1, -1, CELL_COMPUTER):
                    return COMPUTER_WON

        return NEITHER_WON

    # поменять draw на draw_board, иначе не понятно что рисуется из названия переменной
    def draw(self):
        hor_bound = "+" + ("-" * self.n) + "+"
        result = hor_bound + "\n"
        for i in range(self.n):
            result += "|" + "".join(self.state[self.n * i : self.n * (i + 1)]) + "|\n"
        result += hor_bound + "\n"
        return result

    def to_str(self):
        return "".join(self.state)
