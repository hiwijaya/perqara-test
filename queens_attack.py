

class Cell:

    row = 0     # y
    col = 0     # x

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __eq__(self, other):
        return (self.row == other.row) and (self.col == other.col)

    def __str__(self):
        return '(%d,%d)' % (self.row, self.col)


def get_board_and_obstacles_number():

    while True:
        try:
            n, k = input().split()

            n = int(n)
            k = int(k)

            if not (0 < n <= 10 ** 5):
                raise Exception('0 < n <= 10^5')
            if not (0 <= k <= 10 ** 5):
                raise Exception('0 <= k <= 10^5')

            return n, k
        except Exception as e:
            print(e)
            print('Invalid input. try again.')


def get_queen_position(board_number):

    while True:
        try:
            row, col = input().split()

            row = int(row)
            col = int(col)

            if not (1 <= row <= board_number) or not (1 <= col <= board_number):
                raise Exception('Invalid position. Position should inside (%dx%d)' % (board_number, board_number))

            return Cell(row, col)
        except Exception as e:
            print(e)
            print('Invalid input. try again.')


def get_obstacle_positions(board_number, obstacles_number):

    obstacles_positions = []

    while True:
        try:
            row, col = input().split()

            row = int(row)
            col = int(col)

            if not (1 <= row <= board_number) or not (1 <= col <= board_number):
                raise Exception('Invalid position. Position should inside (%dx%d)' % (board_number, board_number))

            obstacles_positions.append(Cell(row, col))

            if len(obstacles_positions) == obstacles_number:
                return obstacles_positions

        except Exception as e:
            print(e)
            print('Invalid input. try again.')


def meet_an_obstacle(given_position, obstacles):

    for obstacle_position in obstacles:
        if given_position == obstacle_position:
            return True

    return False


def get_queens_possible_attack(board_number, queen_position, obstacle_positions):

    possible_attack = 0

    # move to top
    if queen_position.row < board_number:
        for r in range((queen_position.row + 1), board_number + 1):

            moved_position = Cell(r, queen_position.col)
            if meet_an_obstacle(moved_position, obstacle_positions):
                break

            possible_attack += 1

    # move to bottom
    if queen_position.row > 1:
        for r in range((queen_position.row - 1), 0, -1):

            moved_position = Cell(r, queen_position.col)
            if meet_an_obstacle(moved_position, obstacle_positions):
                break

            possible_attack += 1

    # move to left
    if queen_position.col > 1:
        for c in range((queen_position.col - 1), 0, -1):

            moved_position = Cell(queen_position.row, c)
            if meet_an_obstacle(moved_position, obstacle_positions):
                break

            possible_attack += 1

    # move to right
    if queen_position.col < board_number:
        for c in range((queen_position.col + 1), board_number + 1):

            moved_position = Cell(queen_position.row, c)
            if meet_an_obstacle(moved_position, obstacle_positions):
                break

            possible_attack += 1

    # move to top-left
    if (queen_position.row < board_number) or (queen_position.col > 1):

        i = 1
        while True:
            moved_position = Cell((queen_position.row + i), (queen_position.col - i))

            if (moved_position.row > board_number) or (moved_position.col < 1):
                break
            if meet_an_obstacle(moved_position, obstacle_positions):
                break

            possible_attack += 1
            i += 1

    # move to top-right
    if (queen_position.row < board_number) or (queen_position.col < board_number):

        i = 1
        while True:
            moved_position = Cell((queen_position.row + i), (queen_position.col + i))

            if (moved_position.row > board_number) or (moved_position.col > board_number):
                break
            if meet_an_obstacle(moved_position, obstacle_positions):
                break

            possible_attack += 1
            i += 1

    # move to bottom-left
    if (queen_position.row > 1) or (queen_position.col > 1):

        i = 1
        while True:
            moved_position = Cell((queen_position.row - i), (queen_position.col - i))

            if (moved_position.row < 1) or (moved_position.col < 1):
                break
            if meet_an_obstacle(moved_position, obstacle_positions):
                break

            possible_attack += 1
            i += 1

    # move to bottom-right
    if (queen_position.row > 1) or (queen_position.col < board_number):

        i = 1
        while True:
            moved_position = Cell((queen_position.row - i), (queen_position.col + i))

            if (moved_position.row < 1) or (moved_position.col > board_number):
                break
            if meet_an_obstacle(moved_position, obstacle_positions):
                break

            possible_attack += 1
            i += 1

    return possible_attack


if __name__ == '__main__':

    board_number, obstacles_number = get_board_and_obstacles_number()
    queen_position = get_queen_position(board_number)
    obstacle_positions = get_obstacle_positions(board_number, obstacles_number)

    n = get_queens_possible_attack(board_number, queen_position, obstacle_positions)
    print(n)

