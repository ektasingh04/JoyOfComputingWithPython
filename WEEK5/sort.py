#sorting a list--- bubble sort algo... let array 5 1 4 2 8 ...two two elements comparing.. first loop if frst element
# greater than second then swap their pos move fwd.. thus 1 4 2 5 8... second iteration loop--12458.

def bubble(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if(a[j]>a[j+1]):
                tmp=a[j]
                a[j]=a[j+1]
                a[j+1]=tmp


a=[5,4,1,6,7,8]
bubble(a)
for i in a:
    print(i)