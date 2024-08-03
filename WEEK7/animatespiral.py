import turtle
import numpy
turtle.bgcolor("black")
pen=turtle.Turtle()

width=5
height=7
dot_distance=25
pen.setpos(-250,250)
pen.color("white")
pen.fillcolor("purple")
pen.begin_fill()
def spiral(m,n):  #n row n colm and a is matrix input as list of lists
    k=0
    l=0
    f=0

    while(k<m and l<n):
         
        if f==1:
             pen.right(90)
        for i in range(l,n):  #fsrt traverse frst row. means row is fixed we need to traverse the colms only
              pen.color("red")
              pen.forward(dot_distance)
        k=k+1
        f=1
        
        pen.right(90)
        for i in range(k,m):
            pen.color("yellow")
            pen.forward(dot_distance)        
        n=n-1 
        pen.right(90)

        if(k<m):
            for i in range(n-1,l-1,-1): 
                pen.color("white")       
                pen.forward(dot_distance)        #print lowest row.. start from n-1the colm and reach till 1st colm 
                                                # or l-1th col in case of inner rows
            m=m-1     #reduce one row lowest
        pen.right(90)

        if(l<n):  #print 1st com from bottom to up
            for i in range(m-1,k-1,-1):
                 pen.color("green")
                 pen.forward(dot_distance)        
            l=l+1   

pen.end_fill()
spiral(20,20)           