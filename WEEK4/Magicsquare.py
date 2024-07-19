#nxn square grid. sum of each row, colm, diag is constant called magic sum/constant. 
#algo on wikipedia... only odd numbers as n.. M=n(n^2+1)/2.. steps->
# 1 is at (n/2, n-1). let is be(p,q). 2 is at (p-1,q+1).colm becomes 0 make it n.. if row bcm -1 make it n-1
#if calc posn has already a num--> dec colm by 2 and inc row by 1 
# if row posn is -1 and colm posn is n switch to 0,n-2
def magicsq(n):


    magicsquare=[]
    for i in range(n):
        list=[]
        for j in range(n):
            list.append(0)
        magicsquare.append(list)

    i=n//2 #pos of 1
    j=n-1
    
    num=n*n
    count=1

    while(count<=num):
        if(i==-1 and j==n):
            j=n-2
            i=0
        else:
            if(j==n):
                j=0
            if(i<0):        #row bcm -1
                i=n-1
        if(magicsquare[i][j]!=0):
            j=j-2
            i=i-1
            continue # it will skip executing all written below and check from start of loop i.e. the 3 conditions 
                     # bcz it is possibe ki ab b 3 me se koi ek condition bnjaye
        else:
            magicsquare[i][j]=count
            count+=1
        i=i-1       #condn 1
        j=j+1

    for i in range(n):
        for j in range(n):
            print(magicsquare[i][j], end=" ")
        print()

magicsq(3)