import math
print(math.sqrt(16))

import math as m
print(m.sqrt(16))

from math import sqrt
print(sqrt(16))



# random module 

import random
print(random.random())
print(random.randint(1,10))
print(random.choice(['a','b','c']))



import datetime
print(datetime.datetime.now())

now  = datetime.datetime.now()
print(now.year,now.month,now.minute,now.hour,now.second)



import os
print(os.getcwd)
os.chdir('C:\Users\Potla Deekshith\Desktop\wipro-RPS')
print(os.getcwd())
print(os.listdir())
os.makedirs('new_folder')
os.rmdir('new_folder')
os.remove('lk.txt')
os.rename('new_folder','renamed_folder')


path = os.path.join('renamed_folder','mcq.txt')
print(path)
print(os.path.exists('mcq.txt'))
print(os.path.isfile('session_2.py'))
print(os.path.isdir('renamed_folder'))


print(os.path.getsize('session_2.py'))
print(os.path.abspath('session_2.py'))

print(os.environ.get('session_2.py'))



import sys
print(sys.version)
print(sys.path)

print(sys.platform)
print(sys.path)

sys.path.append('renamed_folder')
print(sys.path)


import time
print(time.time())
print(time.ctime())
print(time.localtime())

from collections import Counter
list1 = [1,2,3,4,5,6,7,8,9]
Counter = Counter[list1]
print(Counter)

import random
import string

length = 8
characters = string.ascii_letters + string.digits + string.punctuation
password = ""



class Student:
    def __init__(self , name , age):
        self.name = name
        self.age = age

        def greet(self):
            return f"Hello , my name is  {self.name} and i am {self.age} years old."

s1 = Student("Alics",20)
print(s1.name)
print(s1.age)


for i in range (1,6):
    print("* "*i)




# encapsulation

class Bank:
    def __init__(self):
        self.balance = 1000 #public
        self._temp = 0 #protected
        self.__secret = 1234 #private

b = Bank()
print(b.balnace)
print(b.secret)




# inhertance

class Animal:
    def speak(self):
        print( "animal speaks")
    
class Dog(Animal):
    def barks(self):
        print("dog barks")

d=Dog()
print(d.speak())
print(d.barks())


# polymorpism

class Bird:
    def sound(self):
        print("some sound")


class Sparrow(Bird):
    def sound(self):
        print("sparrow chips")

class Crows(Bird):
    def sound(self):
        print("crow caws")

for bird in (Sparrow(),Crows()):
    bird.sound()




    # abstraction

from abc import ABC , abstractmethod

class payment(ABC):
        @abstractmethod
        def pay(self,amount):
            pass

class UPI(payment):
    def pay(self, amount):
        print("paying {amount} using card")


u1=UPI()
# u2 =card()

u1.pay(100)
# u2.pay(200)





def greeet():
    print("hello ,  world!")
    


class Person:
    def __init__(self , name):
        self.name = name

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self , value):
        self._name=value

p = Person("Alice")
print(p.name)
p.name = "bob"
print(p.name)



class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
p=Person("Alice")
print(p.get_name)






p= Person("alice")
del p._name
print(p._name)



class Person:
    def __init__(self , name):
        self._name=name

    @property
    def name(self):
        return self._name
    
    @name.deleter
    def name(self):
        print("deleting name")
        del self._name

p = Person("alice")
del p.name




class Account:
    def __init__(self , balance):
        self._balance=balance

    @property
    def balance(self):
        return self._balance
    
    @balance.deleter
    def balance(self):
        if self._balance>0:
            raise ValueError("cannot delete with positive amount")