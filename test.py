##Test.py
import piece_class
import board_class

test_board = board_class.board(10) ##Test board of size 10

print "---Now printing the board---"
test_board.printBoard()
print "---Done printing the board---\n"

red_king = piece_class.piece("red", "king")
print "---Placing red_king in all columns of row 1---"
test_board.setLocation(10,1,red_king)
print "---Reprinting board with new pieces---"
test_board.printBoard()
print "---Done printing the board---\n"
