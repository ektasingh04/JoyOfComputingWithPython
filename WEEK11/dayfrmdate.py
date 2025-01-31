#months till july-- odd have 31 days and even have 30 days
#from aug-- odd have 30 even have 31
#python supports from 1970 onlly

import calendar

#year
while 1:
    year=int(input("enter year(1970-2023): "))
    if year<1970:
        print("enter yar after 1970 only")
    else:
        break

#month
while 1:
    month=int(input("enter month(1-12): "))
    if month<=12 and month>0:
        break
    else:
        print("enter correct month from 1 to 12: ")

#check for leap
def check_leap(year):
    if year%100==0:  #for century year divide by 400
        if year%400==0:
            return True
        else:
            return False
    else:      #not century divide by 4
        if year%4==0:
            return True
        else:
            return False

#check for valid date
def check_valid_date(d,m,y,leap):
    if leap:
        if m==2: #feb
            if d<=29:
                return True
            else:
                return False
            
        else: #months aside feb
            if m<8: #till july
                if m%2==0:
                    if d<=30:
                        return True
                    else:
                        return False
                    
                else:
                    if d<=31:
                        return True
                    else:
                        return False
            else:#from august
                if m%2==0:
                    if d<=31:
                        return True
                    else:
                        return False
                    
                else:
                    if d<=30:
                        return True
                    else:
                        return False
    else: #not leap
        if m==2: #feb
            if d<29:
                return True
            else:
                return False
            
        else: #months aside feb
            if m<8: #till july
                if m%2==0:
                    if d<=30:
                        return True
                    else:
                        return False
                    
                else:
                    if d<=31:
                        return True
                    else:
                        return False
            else:#from august
                if m%2==0:
                    if d<=31:
                        return True
                    else:
                        return False
                    
                else:
                    if d<=30:
                        return True
                    else:
                        return False

                
leap=check_leap(year)
#date
while 1:
    date=int(input("enter date: "))
    if date>0 and check_valid_date(date,month,year,leap):
        break
    else:
        print("enter valid date: ")


dayindex=calendar.weekday(year,month,date)
print(dayindex)
def get_day(di):
    daylist=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    return daylist[di] #index of day corresponds to index of that element in list


day=get_day(dayindex)
print(date,'/',month,'/',year,' falls on ',day)