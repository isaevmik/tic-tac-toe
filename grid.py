CELL_EMPTY     = ' '
CELL_PLAYER    = 'X'
CELL_COMPUTER  = 'O'

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

    def valid_coords(self, i, j):
        return (i >= 0 and i < self.n) and (j >= 0 and j < self.n)

    def check(self, i, j, di, dj, c):
        required_to_win = min(5, self.n)
        count = 0

        while count < required_to_win and self.valid_coords(i, j) and self.get(i, j) == c:
            count += 1
            i += di
            j += dj

        return count >= required_to_win

    def who_won(self):
        for row in range(self.n):
            for col in range(self.n):
                if self.check(row, col, +1, 0, CELL_PLAYER):
                    return PLAYER_WON
                elif self.check(row, col, +1, 0, CELL_COMPUTER):
                    return COMPUTER_WON
                elif self.check(row, col, 0, +1, CELL_PLAYER):
                    return PLAYER_WON
                elif self.check(row, col, 0, +1, CELL_COMPUTER):
                    return COMPUTER_WON
                elif self.check(row, col, +1, +1, CELL_PLAYER):
                    return PLAYER_WON
                elif self.check(row, col, +1, +1, CELL_COMPUTER):
                    return COMPUTER_WON
                elif self.check(row, col, +1, -1, CELL_PLAYER):
                    return PLAYER_WON
                elif self.check(row, col, +1, -1, CELL_COMPUTER):
                    return COMPUTER_WON

        return NEITHER_WON

    def draw(self):
        hor_bound = '+' + ('-' * self.n) + '+'
        result = hor_bound + '\n'
        for i in range(self.n):
            result += '|' + ''.join(self.state[self.n * i : self.n * (i + 1)]) + '|\n'
        result += hor_bound + '\n'
        return result

    def to_str(self):
        return ''.join(self.state)
