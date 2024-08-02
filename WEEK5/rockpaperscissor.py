def rps(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3 #placeholder in num1
    p2=int(num2[bit2])%3
    if (pl1[p1]==pl2[p2]):
        print("draw")
    elif (pl1[p1]=="rock" and pl2[p2]=="scissor"):
        print("player 1 won")
    elif (pl1[p1]=="rock" and pl2[p2]=="paper"):
        print("player 2 won")
    elif (pl1[p1]=="paper" and pl2[p2]=="scissor"):
        print("player 2 won")
    elif (pl1[p1]=="paper" and pl2[p2]=="rock"):
        print("player 1 won")
    elif (pl1[p1]=="scissor" and pl2[p2]=="paper"):
        print("player 1 won")
    elif (pl1[p1]=="scissor" and pl2[p2]=="rock"):
        print("player 2 won")



pl1={0:'rock',1:'paper',2:'scissor'}
pl2={0:'paper',1:'rock',2:'scissor'}
while(1):
    num1=input("player 1 enter ur choice")
    num2=input("player 2 enter ur choice")
    bit1=int(input("p1 enter the secret bit pos "))
    bit2=int(input("p2 enter the secret bit pos "))
    rps(num1,num2,bit1,bit2)
    ch=input("do u want to continue: Y or N")
    if(ch=='N'):
        break
