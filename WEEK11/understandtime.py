''' calender datetime and pytz(timezone) libs'''

from datetime import datetime as dt
import pytz
import calendar
from datetime import datetime as dt
print(dt.now()) #yyyy mm dd hr min secc milisec


x=dt.now()
#create a timezone object
tmz=pytz.timezone('Singapore')
print(dt.now(tmz)) #shows current time as well as how many hrs it is GMT+

pytz.all_timezones  #list of timezones- 596
print(dt.time.time())
print(calendar.weekday(2004,7,12)) #0-6~ monday-sunday
print(x.strftime('%A'))