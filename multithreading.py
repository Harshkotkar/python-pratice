import time
import threading

def wakeup():
    time.sleep(2)
    print("u  just wakeup")

def breakfast():
    print("U just started the breakfast")
    time.sleep(2)
    print("u have finished the breakfast")

def school():
    time.sleep(2)
    print("u have arived the school")

def coffe():
    time.sleep(1)
    print("u have finshed the coffe")
def study():
    time.sleep(1)
    print("U have finshed your study")

x=threading.Thread(target=wakeup,args=())
x.start()
y=threading.Thread(target=breakfast,args=())
y.start()
z=threading.Thread(target=school,args=())
z.start()
l=threading.Thread(target=coffe,args=())
l.start()
m=threading.Thread(target=study,args=())
m.start()

x.join()
y.join()
z.join()
l.join()
m.join()

# wakeup()
# breakfast()
# school()
# coffe()
# study()
print(threading.active_count())

print(threading.enumerate())
print(time.perf_counter())
