import random
year=random.randint(1993,2023)
print(year)
if(year%4==0 and year%100!=0 or year%400==0):
    print("give year is leap")
else:
    print("not leap")