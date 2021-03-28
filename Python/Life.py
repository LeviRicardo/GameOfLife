from random import choice as rd
from time import sleep as slp

def mount_board(h=15,w=50): # Creates a board using the parameters as size
    chances = 3 #Chances of life existing in percentage
    possibilities = [" " if i!= round(100/chances) else "#" for i in range(1, round(100/chances)+1)]
    board = [ [] for i in range(h)]
    for linhas in range(len(board)):
        board[linhas] = [rd(possibilities) for i in range(w)]
    return(board)   

def next_board(board):
    next_board = board
    



    return next_board

first_board = mount_board()
present_board = first_board
att_time = 0.1


print(first_board)
for i in range(5):
#    print("-------------------------------------------------------------")
    present_board = next_board(present_board)
    [print("".join(i)) for i in present_board]
    slp(att_time)