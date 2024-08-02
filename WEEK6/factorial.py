#iterative
def ifact(n):
    product=1
    if n==0:
        return 1
    for i in range(1,n+1):
        product=product*i
    return product


#recursive
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

 
    
print("iterative factorial of 5 ", ifact(5))
n=int(input("enter a +ve number "))
if (n<0):
    print("enter only posotive")
else:
    print("factoial by recursive method of ",n," is ",fact(n))