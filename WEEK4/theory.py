# datetime library
import datetime
datetime.date.today()
datetime.date.today().strftime("%Y")
 #displays only year B for month d for day
datetime.date.today().strftime("%W")
# week no. for week day ->%w, for day of year->j
# for name of day of week-A

day=datetime.datetime.now() #year,month,date,hr,min,sec
print(day)

# another way for declarin a matrix is 
magic=[ 0 for i in range(3)] #prints 3 zeroes in a row
magic1=[[0 for i in range(3)] for j in range(3)]
print(magic)
print(magic1)

# other way
matrix=[]
for i in range(3):
    l=[]
    for j in range(3):
        l.append(0)
    matrix.append(l)
for i in range(3):
    for j in range(3):
        print(matrix[i][j], end=" ")
    print()
     
