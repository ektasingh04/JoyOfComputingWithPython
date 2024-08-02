# three doors two of them comprises of goods and one of them comprises of a 
#price say bmw in this whole programme screen cast we will be using bmw as the price.
#So in Monte hall problem participant is asked to choose any one of this doors, after he or she 
#had made his or her choice the host ask the participant to change his choice whatthe host 
#basically does here is he opens a particular door out of these three doors oknow we are left with 
#only two doors one that has been chosen by the participant and onethat has been opened yet so #
#now the host ask the participant to change his choice, it dependson the participant to swap or not swap his or her 
#choice now what the participant dohere is should he swap or not swap this is the question that we should answer ok so thisseems question 
#will be exploring will be answering in the programming screen cast will have akind of setup here in which we have three doors two of them 
#comprise of goods and oneof them comprise of bmw after the choice whether the participant swapped or not swapped wewill we will try to 
#explore this fact that what is the optimal strategy here, whetherthe participant should swap or not swap

import random
doors=[0]*3
print(doors)
goatdoor=[0]
print(goatdoor)
swap=0
notswap=0 #count of wins in swap and non swap cases
j=0
while(j<5):
    x=random.randint(0,2)
    for i in range(0,3):
        if (i==x):
            doors[i]="bmw"
        else:
            doors[i]="goat"
            goatdoor.append(i)

    choice=int(input("enter your choice"))
    dopen=random.choice(goatdoor)
    while(dopen==choice):
        dopen=random.choice(goatdoor)
    ch2=input("do u want to swap: 1 for yes or 2 for no")
    if (ch2==2):
        if (doors[choice]=="goat"):
             print("you lost")
        else:
            print("you won")
            notswap=notswap+1
    else:
        if(doors[choice]=="goat"):
            print("you won")
            swap=swap+1
        else:
            print("you lost")
    j=j+1

print(swap)
print(notswap)