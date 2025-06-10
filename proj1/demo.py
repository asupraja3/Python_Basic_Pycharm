from Calc import *
class Computer:
    def config(self):
        print("i5,16GB")

a = '8'
print(type(a))
#str is an inbuilt class: see the output
#As everything is an object in Python
comp1 = Computer()
print(type(comp1))

#1.one way of calling a method
comp1.config()
#2.second way of calling method
Computer.config(comp1)
a=5
a.bit_length()