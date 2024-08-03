import numpy

def spiral(m,n,a):  #n row n colm and a is matrix input as list of lists
    k=0
    l=0
    ''' k is starting row and l is starting colm'''

    while(k<m and l<n):
         
         #1st row print
        for i in range(l,n):  #fsrt traverse frst row. means row is fixed we need to traverse the colms only
              print(a[k][i],end=" ")

         #now we have to print last colm starting from 2nd row so increase row by 1
        k=k+1

        for i in range(k,m):
             print(a[i][n-1], end=" ")
        
        n=n-1 #  one colm reduced  last col

        if(k<m):
            for i in range(n-1,l-1,-1):        #-1 shows the step ,,, by default it is 1 always
                  print(a[m-1][i],end=" ")      #print lowest row.. start from n-1the colm and reach till 1st colm 
                                                # or l-1th col in case of inner rows
            m=m-1     #reduce one row lowest

        if(l<n):  #print 1st com from bottom to up
            for i in range(m-1,k-1,-1):
                  print(a[i][l])
            l=l+1   


#create  matrix
a=[]
count=1  
for i in range(4):  #cols
     l=[]
     for j in range(4):
          l.append(count)  #rows
          count+=1
     a.append(l)

spiral(4,4,a)
print(numpy.matrix(a))