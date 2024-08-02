#our colm row start from 1 1 but comp starts from 0 0 isliye we reduce 1 1 from our calculn of r and c
# 2 plyrs each given 2 symls x o.. fill at vacant cells.. one who attains same symbl in 3 rows,colms or diagonals
#wins the game .. if no one does then draw
import numpy 
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']]) 
#array need to defined as list of lists.. rows are written in list format and then those rows become elemnts as colm list

ps1='X'
ps2='O'
def place(symb):
    print(numpy.matrix(board)) #prints the list format into matrix format
    while(1):
      row=int(input('enter row posintion 1or 2 or 3 :'))
      col=int(input("enter colm number 1 or 2 or 3: "))
      if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-':
          break
      else:
          print("invalid input")
          continue
    board[row-1][col-1]=symb


def check_rows(symb):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symb :
                count=count+1
        if count==3:
            print(symb+" won ")
            return True
    return False
        
def check_col(symb):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symb :
                count=count+1
        if count==3:
            print(symb+" won ")
            return True
    return False   


def check_diag(symb):
    if (board[0][0]==board[1][1]==board[2][2]== symb) or (board[2][0]==board[1][1]==board[0][2]== symb):
        print(symb+" won ")
        return True
    else:
        return False

def won(symb):
    return check_rows(symb) or check_col(symb) or check_diag(symb)
    
def play():
    #9 cells so 9 turns at max
    for turn in range(9):
        if (turn%2==0):
            print('X turn')
            place(ps1)
            if won(ps1):
                break
        else:
            print('O turn')
            place(ps2)
            if won(ps2):
                break      
    if not(won(ps1)) and not(won(ps2)):
            print("draw")    
 
play()