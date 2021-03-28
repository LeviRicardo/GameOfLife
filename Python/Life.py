from random import choice as rd
from time import sleep as slp

def mount_board(h=15,w=50, chances=3): # Creates a board using the parameters as size    
    #chances = Chances of life existing in percentage
    #h,w = Height and width of the board
    possibilities = [" " if i!= round(100/chances) else "#" for i in range(1, round(100/chances)+1)]
    board = [ [] for i in range(h)]
    for rows in range(len(board)):
        board[rows] = [rd(possibilities) for i in range(w)]
    return board 

def next_board(board2):
    next_board = []
    next_board.extend(board2)
    for rows in range(len(board2)):
        for columns in range(len(board2[rows])):
            total = int(checking(board2,rows,columns))
            if board2[rows][columns] == "#" and total not in [2,3]:
                print("Morre")
                #next_board[rows][columns] = " "
            elif board2[rows][columns] == "#" and total in [2,3]:
                print("Vive")
                #next_board[rows][columns] = "#"
            elif board2[rows][columns] == " " and total == 3:
                print("Revive")
                #next_board[rows][columns] = "#"
    return next_board

def checking(board3, row, column):
    board4 = board3[:]
    indexes = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    counter = 0
    for i in indexes:
        try:
            if row+i[0] < 0 or column+i[1]<0:
                continue
            if board4[row+i[0]][column+i[1]] == "#":
                counter += 1
        except IndexError:
            pass
    return counter

#first_board = mount_board(h=5,w=5,chances=20)
#present_board = first_board
att_time = 0.1
rounds = 1
present_board = [["#","#","#"," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "]]

#[print("".join(i)) for i in present_board]
for i in range(rounds):
 #   print("-------------------------------------------------------------")
    present_board = next_board(present_board)
  #  [print("".join(i)) for i in present_board]
   # slp(att_time)