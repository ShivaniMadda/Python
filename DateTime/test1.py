from datetime import datetime
import time


date_time = datetime.fromtimestamp(1346236702)
print(date_time)
print("------------------------------")
print(type(date_time))
print("------------------------------")
print(str(date_time))
print("------------------------------")
print(type(str(date_time)))
print("------------------------------")



time_stamp = time.mktime(date_time.timetuple())
print(time_stamp)
print("------------------------------")
print(type(time_stamp))
print("------------------------------")
print(int(time_stamp))
print("------------------------------")
print(type(int(time_stamp)))



date_string = "2012-12-12 10:10:10"
s = datetime.fromisoformat(date_string)
print(s)
print(type(s))