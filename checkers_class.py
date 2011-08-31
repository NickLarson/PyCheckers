import piece_class ##Need create piece
import board_class ##Need set location

class checkers():
    """
    This will create the actual checkers board used to play.
    """
    def __init__(self, size):
        new_board = board_class.board(size)
        self.board = new_board
        red_piece = piece_class.piece("red", "regular")
        black_piece = piece_class.piece("black", "regular")
        for row in range(1,4): ##This is going to set up the first player's pieces
            for column in range(1,11):
                if row%2 == 0 and column%2 != 0:
                    new_board.setLocation(column, row, red_piece)
                    print red_piece.printPiece(), row, column
                if row%2 != 0 and column%2 == 0:
                    new_board.setLocation(column, row, red_piece)
                    print red_piece.printPiece(), row, column
        for row in range(6,9): ##This is going to set up the first player's pieces
            for column in range(1,11):
                if row%2 == 0 and column%2 != 0:
                    new_board.setLocation(column, row, red_piece)
                    print black_piece.printPiece(), row, column
                if row%2 != 0 and column%2 == 0:
                    new_board.setLocation(column, row, red_piece)
                    print black_piece.printPiece(), row, column    
             

