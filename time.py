import time
print(time.ctime(1000000))


print(time.time())

time_obj=time.localtime()
print(time_obj)
local_time=time.strftime("%B %d %Y %H:%M:%S",time_obj)
print(local_time)
#(year,month,day,hr,min,sec, #day of the week,#day of the year,dst)

time_tuple=(2024,4,20,4,20,0,0,0,0)
time_str=time.asctime(time_tuple)
print(time_str)