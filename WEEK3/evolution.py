#here we have a file dna with info in bytes 0 and 1 as we change 1 or 0 the info changes
import random
def evolve(x):
    index=random.randint(1,len(x)-1)
    p=random.randint(1,100)
    if p==1:
        if x[index]=='0':
            x[index]='1'
        else:
            x[index]='0'

with open("C:\\Users\\dell\\projects\\helloworld\\PYTHON\\WEEK3\\file.txt","r+") as myfile:
    x=myfile.read()
    x=list(x)
for i in range(1,100):
    evolve(x)
print(x)