import random
import matplotlib.pyplot as plt


x=[]
y=[]

account=0

for i in range(365):
    x.append(i)
    bet=random.randint(1,10)
    luckydraw=random.randint(1,10)
    if bet==luckydraw:
        account=account+900-100
    else:
        account=account-100
    y.append(account)
    

print(" final sum in account ", account)
plt.plot(x,y)
plt.show()