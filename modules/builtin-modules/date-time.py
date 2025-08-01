
# import datetime module
import datetime as dt

# working with time class
time = dt.time
t = time(6,35,22,34) # store time
print(t)
t2 = time() # parameters are optional
print(t2)
# using time class object you caan access all its attributes
print(t.hour,t.minute,t.tzinfo)

# methods of time class

print(t.isoformat())
print(t.strftime("%I %M %p"))
new_t = t.replace(minute=45) # returns new time object
print(new_t)
# You can compare time objects but not add or subtract
t_one = time(12,33,44)
t_two = time(12,33,44)
print(t_one == t_two)
t_one = t_one.replace(minute=20)
print(t_one < t_two)

# working with date class

momin_dob = dt.date(2003,12,24) # store any date
print(momin_dob)

current_date = dt.date.today()
print(current_date)
print(current_date.year)
print(current_date.day)
print(current_date.month)

print(current_date.isoformat())
print(current_date.strftime("%B-%Y-%m"))
# create date from string

dd = dt.date.fromisoformat("2003-10-04")
print(dd)

print(dd.isoweekday()) # 1 to 7
print(dd.weekday()) # 0 to 6

# working with datetime class

current_time = dt.datetime.now().time()
print(current_time)
now_date = dt.datetime.now().date()
print(now_date)
