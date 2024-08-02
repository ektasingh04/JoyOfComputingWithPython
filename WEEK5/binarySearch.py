#need the data be sorted...

def binary(a,x):
    first=0
    last=len(a)-1
    flag=0 
    count=0
    while(first<=last and flag==0):
        mid=(first+last)//2
        count+=1
        if(mid==x):
            flag=1
            print("element found at "+ str(mid))
            print("number of iterations "+ str(count))
            return
        else:
            if (x<a[mid]):
                last=mid-1
            else:
                first=mid+1

    print("number not found")

a=[]
for i in range(1,101):
    a.append(i)
binary(a,55)
