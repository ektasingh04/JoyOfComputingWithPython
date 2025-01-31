import random
word=input("enter" )
l=[]
total=1
for i in range(1,len(word)+1):
    total=total*i
while len(l)<total:
    j="".join(random.sample(word,len(word)))
    l.append(j)
for each in l:
    print (each)