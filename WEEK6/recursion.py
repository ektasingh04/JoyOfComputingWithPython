#binary search by recusrion
def bin(l,x,start,end):
    #base case--> both start end at one element only one elmet in list
    if start==end:
        if l[start]==x:
            return start
        else:
            return -1
    else:
        #divide in 2 halves and then search
        mid=int((start+end)/2)
        if l[mid]==x:
            return mid
        elif l[mid]>x:
            return bin(l,x,start,mid-1)
        else:
            return bin(l,x,mid+1,end)
        
l=[10,20,30,40,45,46]
x=int(input("enter key "))
if(bin(l,x,0,len(l)-1)==-1):
    print("not found")
print("index is ", bin(l,x,0,len(l)-1)) #u can print index+1 as index starts from 0 in an list..

