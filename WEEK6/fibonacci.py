
def fib(n):
    #f(0)=0 f(1)=1 f(n)=f(n=2)+f(n-1)
    if n<2:
        return n
    else:
        return fib(n-1)+fib(n-2)
    
print(fib(4))