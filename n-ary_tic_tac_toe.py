def create_board(size: int):
    """Creates a tic-tac-toe board of dimension size x size"""
    x_length = range(size)
    y_length = range(size)
    output_board = []

    for x, y in zip(x_length, y_length):
        print(x, y)
        if x == 0:
            output_board.append('x ')
            print('x ', end='')
        else:
            output_board.append('| x ')
            print('| x ')
    
    return output_board

create_board(3)
