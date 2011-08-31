##Test.py
import piece_class
import board_class

test_board = board_class.board(10) ##Test board of size 10

print "---Now printing the board---"
test_board.printBoard()
print "---Done printing the board---\n"

red_king = piece_class.piece("red", "king")
print "---Placing red_king in all columns of row 1---"
for i in range(1,11):
    test_board.setLocation(1,i,red_king)
print "---Reprinting board with new pieces---"
test_board.printBoard()
print "---Done printing the board---\n"
print "---Attempting to make illegal sets...---"
blue_queen = piece_class.piece("blue", "queen")
for i in range(1,11):
    test_board.setLocation(1,i, blue_queen)
print "---Attempting to move queens to all positions in row 2---"
for i in range(1,11):
    test_board.setLocation(2,i,blue_queen)
print "---Reprinting board with new pieces---"
test_board.printBoard()
print "---Done printing the board---\n"
green_king = piece_class.piece("green", "queen")
print "---Attempting to move green queens to all positions in row 10---"
for i in range(1,11):
    test_board.setLocation(10,i,blue_queen)
print "---Reprinting board with new pieces---"
test_board.printBoard()
print "---Done printing the board---\n"
