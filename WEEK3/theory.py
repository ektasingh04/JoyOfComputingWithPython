with open("C:\\Users\\dell\\projects\\helloworld\\PYTHON\\WEEK3\\file.txt","r+") as myfile:
    print(myfile.read())
    myfile.write("I am fine.")
    print(myfile.read())
    
myfile.close()
import random
#randint includes both the 1 and 5
pr=random.randint(1,5)
print(pr)
#randrange can print 1 but not 5 i.e. the upper range
#random.random genertes decimals from 0 to 1
random.randrange(1,10,2)
#this will put step in geration only odds will be printed if want to even  start from 2
#random.choice({1,2,3,4})--nonly from list list={11,2,3,4,44} random.choice(list)