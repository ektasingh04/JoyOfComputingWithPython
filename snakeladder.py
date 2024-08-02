#snake takes from higher to lower while ladder takes u from lower to higher
#snakes-64 to 36 98 to
#ladders 

#high leveel view-- show the board play the game one who reaches end ie 100 wins

from PIL import Image
import string
import random
end=100

def show_board():
    img=Image.open('WEEK7\snl.png')
    img.show()
    
def check_ladder(points):
    if points==4:
        print(" u stepped on ladder")
        return 56
    elif points==12:
        print(" us tepped on ladder ")
        return 50
    elif points==14:
        print(" us tepped on ladder ")
        return 55
    elif points==22:
        print(" us tepped on ladder ")
        return 58
    elif points==41:
        print(" us tepped on ladder ")
        return 79
    elif points==54:
        print(" us tepped on ladder ")
        return 88
    else:
        #no ladder
        return points
    

def reached_end(points):
    if points==end:
        return True
    else:
        return False

def check_snake(points):
    if points==28:
        print(" us tepped on snake ")
        return 10
    elif points==37:
        print(" us tepped on snake ")
        return 3
    elif points==47:
        print(" us tepped on snake ")
        return 16
    elif points==75:
        print(" us tepped on snake ")
        return 32
    elif points==94:
        print(" us tepped on snake ")
        return 71
    elif points==96:
        print(" us tepped on snake ")
        return 42
    else:
        return points

def play():
    p1name=input('enter 1st player name')     
    p2name=input('enter 2nd player name')
    pp1=0 #initial points of p1
    pp2=0

    turn=0
    while(1):       #break the loop when one player reaches end point
        if turn%2==0:  #p1
            print(p1name +" your turn")
            #ask for choice to continue
            c=input("enter 1 to continue 0 to quit")
            if c==0:
                print("points of both players are : ", p1name," scored= ",pp1,"\t",p2name," scored= ",pp2)
                print("quitting the game. thank you")
                break
            else: #roll a dice
                dice=random.randint(1,6)
                print("dice showes ",dice)
                #update the points acc to dice
                pp1=pp1+dice
                #now check if u reached a ladder or snake
                pp1=check_ladder(pp1)  #checkladder checks if pp1 is a bottom of ladder and return updated pp1
                pp1=check_snake(pp1)
                #if player goes beyond the board
                if pp1>end:
                    pp1=end
                print(p1name," your score ",pp1)

                if reached_end(pp1):
                    print(p1name, " won ")
                    break
        else:  #p2 
            print(p2name+" ur turn ")
            #ask for choice to continue
            c=input("enter 1 to continue 0 to quit")
            if c==0:
                print("points of both players are : ", p1name," scored= ",pp1,"\t",p2name," scored= ",pp2)
                print("quitting the game. thank you")
                break
            else: #roll a dice
                dice=random.randint(1,6)
                print("dice showes ",dice)
                #update the points acc to dice
                pp2=pp2+dice
                #now check if u reached a ladder or snake
                pp2=check_ladder(pp2)  #checkladder checks if pp1 is a bottom of ladder and return updated pp1
                pp2=check_snake(pp2)
                #if player goes beyond the board
                if pp2>end:
                    pp2=end
                print(p2name," your score ",pp2)

                if reached_end(pp2):
                    print(p2name, " won ")
                    break

        turn=turn+1  #increment turn for next players turn



show_board()
play()
