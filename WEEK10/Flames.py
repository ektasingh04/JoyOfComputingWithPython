import string

def removematching(l1,l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i]==l2[j]:
                c=l1[i]
                l1.remove(c)
                l2.remove(c)
                l=l1+["*"]+l2 #contancate two lists
                return [l,True]
    l=l1+["*"]+l2
    return [l,False]



p1=input("enter first person name ")
p2=input(" enter second person name ")
p1=p1.lower()
p1=p1.replace(" ","")
p2=p2.lower()
p2=p2.replace(" ","")

l1=list(p1)
l2=list(p2)

proceed=True
while proceed:
    returnedlist=removematching(l1,l2)
    contlist=returnedlist[0]
    proceed=returnedlist[1]
    starindex=contlist.index('*')
    l1=contlist[:starindex]  #l1 is from 0 to before star l2 is from next to star to end
    l2=contlist[starindex+1:]

count=len(l1)+len(l2)
result=['freinds','love','affection','marriage','enemy','siblings']

while len(result)>1:
    splitindex=(count%len(result)) -1
    if splitindex>=0:
        right=result[splitindex+1:]
        left=result[:splitindex]
        result=right+left
    else:
        result = result[:(len(result)-1)]

print(result[0])
