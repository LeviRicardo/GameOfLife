from random import choice as rd
from time import sleep as slp

def mount_board(h=15,w=50, chances=3): # Creates a board using the parameters as size    
    #chances = Chances of life existing in percentage
    #h,w = Height and width of the board
    possibilities = [" " if i!= round(100/chances) else "#" for i in range(1, round(100/chances)+1)]
    board = [ [] for i in range(h)]
    for rows in range(len(board)):
        board[rows] = [rd(possibilities) for i in range(w)]
    return(board)   

def next_board(board):
    next_board = list(board)
    for rows in range(len(board)):
        for columns in range(len(board[rows])):
            total = checking(board,rows,columns)
            if next_board[rows][columns] == "#":
                if total < 2 or total > 3:
                    next_board[rows][columns] = " "
                else:
                    next_board[rows][columns] = "#"
            else:
                if total == 3:
                    next_board[rows][columns] = "#"
    return next_board

def checking(board, row, column):
    board = board[:]
    indexes = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    counter = 0
    for i in indexes:
        try:
            if row+i[0] < 0 or column+i[1]<0:
                continue
            if board[row+i[0]][column+i[1]] == "#":
                counter += 1
        except IndexError:
            pass
    return counter

first_board = mount_board(h=5,w=5,chances=20)
present_board = first_board
att_time = 0.1
rounds = 3
present_board = [["#","#","#"," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "]]

[print("".join(i)) for i in present_board]
for i in range(rounds):
    print("-------------------------------------------------------------")
    present_board = next_board(present_board)
    [print("".join(i)) for i in present_board]
    slp(att_time)