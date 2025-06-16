#Multithreading
from time import sleep
from threading import *
class hello(Thread):
  def run(self): #Inside Thread class there is run method
    for i in range(5):
      print("Hello")
      sleep(1)

class hi(Thread):
  def run(self):
    for i in range(5):
      print("Hi")
      sleep(1)

t1 = hello()
t2 = hi()

t1.start() #Use start method which will call run()
sleep(0.2)
t2.start()
#there are 3 threads main thread, t1 thread, t2 thread
print("before Bye") #Main prints this
t1.join() #Wait for t1 to finish
t2.join() #Wait for t2 to finish

print("last Bye") #Main prints this after t1 and t2 finish

# This code demonstrates the use of multithreading in Python using functions
import threading

def print_numbers():
    for i in range(5):
        print(i)

t1 = threading.Thread(target=print_numbers)
t1.start()
t1.join()
