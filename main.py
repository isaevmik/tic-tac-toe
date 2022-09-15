import grid
import minmax

def computer_step(g):
    n = g.n
    for i in range(n):
        for j in range(n):
            if g.get(i, j) == grid.CELL_EMPTY:
                g.set(i, j, grid.CELL_COMPUTER)
                result = minmax.player_wins(g)
                if not result:
                    return
                g.set(i, j, grid.CELL_EMPTY)
    for i in range(n):
        for j in range(n):
            if g.get(i, j) == grid.CELL_EMPTY:
                g.set(i, j, grid.CELL_COMPUTER)
                return

def player_step(g):
    print(g.draw())
    while True:
        i, j = list(map(int, input("Enter row and column: ").split(' ')))
        i, j = i - 1, j - 1
        if g.valid_coords(i, j) and g.get(i, j) == grid.CELL_EMPTY:
            g.set(i, j, grid.CELL_PLAYER)
            break
        else:
            print('Invalid coordinates!')

def main():
    n = int(input("Enter grid size: "))
    g = grid.Grid(n)
    empty_cells = n * n
    while True:
        computer_step(g)
        if g.who_won() == grid.COMPUTER_WON:
            print('Computer won!')
            return
        empty_cells -= 1
        if empty_cells == 0:
            print('Neither won!')
            return
        player_step(g)
        if g.who_won() == grid.PLAYER_WON:
            print('Player won!')
            return
        empty_cells -= 1
        if empty_cells == 0:
            print('Neither won!')
            return

if __name__ == '__main__':
    main()
