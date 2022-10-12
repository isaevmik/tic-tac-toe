import unittest

import grid
import minmax


# Аналогично с main. Надо везде переименовать g, выглядит, как не информативное название переменной.
# В целом все однобуквенные переменные лучше назвать как-нибудь более информативно


def grid_from_str(s):
    lines = s.splitlines()
    n = len(lines)
    for line in lines:
        assert len(line) == n
    g = grid.Grid(n)
    # i, j -> row, columns
    for row in range(n):
        for columns in range(n):
            if lines[row][columns] != " ":
                g.set(row, columns, lines[row][columns])
    return g


# One Assert per Test rule
# http://www.owenpellegrin.com/blog/testing/how-do-you-solve-multiple-asserts/s
class TestGrid(unittest.TestCase):
    def test_empty(self):
        for n in range(1, 10):
            with self.subTest():
                g = grid.Grid(n)

                self.assertFalse(g.valid_coords(-1, 0))
                self.assertFalse(g.valid_coords(n, 0))
                self.assertFalse(g.valid_coords(0, n))

                for i in range(n):
                    for j in range(n):
                        self.assertEqual(g.get(i, j), grid.CELL_EMPTY)

                self.assertEqual(g.who_won(), grid.NEITHER_WON)

    def test_row(self):
        for n in range(1, 10):
            required_to_win = min(5, n)
            for (c, v) in [
                (grid.CELL_COMPUTER, grid.COMPUTER_WON),
                (grid.CELL_PLAYER, grid.PLAYER_WON),
            ]:
                with self.subTest():
                    g = grid.Grid(n)
                    for j in range(0, required_to_win):
                        g.set(0, j, c)
                    self.assertEqual(g.who_won(), v)

    def test_column(self):
        for n in range(1, 10):
            required_to_win = min(5, n)
            for (c, v) in [
                (grid.CELL_COMPUTER, grid.COMPUTER_WON),
                (grid.CELL_PLAYER, grid.PLAYER_WON),
            ]:
                with self.subTest():
                    g = grid.Grid(n)
                    for i in range(0, required_to_win):
                        g.set(i, 0, c)
                    self.assertEqual(g.who_won(), v)

    def test_diag1(self):
        for n in range(1, 10):
            required_to_win = min(5, n)
            for (c, v) in [
                (grid.CELL_COMPUTER, grid.COMPUTER_WON),
                (grid.CELL_PLAYER, grid.PLAYER_WON),
            ]:
                with self.subTest():
                    g = grid.Grid(n)
                    for i in range(0, required_to_win):
                        g.set(i, i, c)
                    self.assertEqual(g.who_won(), v)

    def test_diag2(self):
        for n in range(1, 10):
            required_to_win = min(5, n)
            for (c, v) in [
                (grid.CELL_COMPUTER, grid.COMPUTER_WON),
                (grid.CELL_PLAYER, grid.PLAYER_WON),
            ]:
                with self.subTest():
                    g = grid.Grid(n)
                    for i in range(0, required_to_win):
                        g.set(i, n - 1 - i, c)
                    self.assertEqual(g.who_won(), v)

    def test_player_wins(self):
        grid_strings = ["XOO\n X \n O ", "XXX\nXXX\nXXX", "XXX\nX X\nX  "]
        for g in map(grid_from_str, grid_strings):
            with self.subTest():
                self.assertTrue(minmax.player_wins(g))

    def test_computer_wins(self):
        grid_strings = ["O O\n   \n   ", "O  \n   \nO  "]
        for g in map(grid_from_str, grid_strings):
            with self.subTest():
                self.assertTrue(minmax.computer_wins(g))


if __name__ == "__main__":
    unittest.main()
