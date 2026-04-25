# import math
# print(math.sqrt(16))

# import math as m
# print(m.sqrt(16))

# from math import sqrt
# print(sqrt(16))



# random module
# import random
# print(random.random())
# print(random.randint(1,10))
# print(random.choice(['a','b','c']))



# import datetime
# print(datetime.datetime.now())

# now  = datetime.datetime.now()
# print(now.year,now.month,now.minute,now.hour,now.second)



# import os
# print(os.getcwd)
# os.chdir('C:\Users\Potla Deekshith\Desktop\wipro-RPS')
# print(os.getcwd())
# print(os.listdir())
# os.makedirs('new_folder')
# os.rmdir('new_folder')
# os.remove('lk.txt')
# os.rename('new_folder','renamed_folder')


# path = os.path.join('renamed_folder','mcq.txt')
# print(path)
# print(os.path.exists('mcq.txt'))
# print(os.path.isfile('session_2.py'))
# print(os.path.isdir('renamed_folder'))


# print(os.path.getsize('session_2.py'))
# print(os.path.abspath('session_2.py'))

# print(os.environ.get('session_2.py'))



# import sys
# print(sys.version)
# print(sys.path)

# print(sys.platform)
# print(sys.path)

# sys.path.append('renamed_folder')
# print(sys.path)


# import time
# print(time.time())
# print(time.ctime())
# print(time.localtime())

# from collections import Counter
# list1 = [1,2,3,4,5,6,7,8,9]
# Counter = Counter[list1]
# print(Counter)

# import random
# import string

# length = 8
# characters = string.ascii_letters + string.digits + string.punctuation
# password = ""



# class Student:
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age

#         def greet(self):
#             return f"Hello , my name is  {self.name} and i am {self.age} years old."

# s1 = Student("Alics",20)
# print(s1.name)
# print(s1.age)


# for i in range (1,6):
#     print("* "*i)




#encapsulation

# class Bank:
#     def __init__(self):
#         self.balance = 1000 #public
#         self._temp = 0 #protected
#         self.__secret = 1234 #private

# b = Bank()
# print(b.balnace)
# print(b.secret)




#inhertance

# class Animal:
#     def speak(self):
#         print( "animal speaks")
    
# class Dog(Animal):
#     def barks(self):
#         print("dog barks")

# d=Dog()
# print(d.speak())
# print(d.barks())


#polymorpism

# class Bird:
#     def sound(self):
#         print("some sound")


# class Sparrow(Bird):
#     def sound(self):
#         print("sparrow chips")

# class Crows(Bird):
#     def sound(self):
#         print("crow caws")

# for bird in (Sparrow(),Crows()):
#     bird.sound()




    #abstraction

# from abc import ABC , abstractmethod

#     class payment(ABC):
#         @abstractmethod
#         def pay(self,amount):
#             pass

# class UPI(payment):
#     def pay(self, amount):
#         print("paying {amount} using card")


# u1=UPI()
# u2 =card()

# u1.pay(100)
# u2.pay(200)




#      ASSIGNMENT- 1

# class Student:
#     def __init__(self, name , age):
#         self.name= name
#         self.age=age

#     def display(self):
#         print(self.name)
#         print(self.age)

# # task 1

# s1 = Student("Deekshith",21)
# s2 = Student("Naveen",22)
# print(s1.name , s2.age)
# print(s2.name , s2.age)


#  # task 2

# s1.display()

# # task 3

# class Rectangle:
#     def __init__(self , lenght , width):
#         self.lenght =lenght
#         self.width = width

#     def area(self):
#         return self.lenght * self.width
    
# areaOfRectange = Rectangle(10 , 5)
# print(areaOfRectange.area())


#   task 4

# class car:
#     def __init__(self , brand , price):
#         self.brand = brand
#         self.price = price

#     def display_details(self):
#         print(self.brand)
#         print(self.price)

# carDetails = car("BMW" , 2500000)
# print(carDetails.display_details())


#   task 5

# class Employee:
#     def __init__(self , name , salary):
#         self.name =name
#         self.salary = salary
#     def details(self):
#         print(self.name)
#         print(self.salary)

# e = Employee("Deekshith" , 25000)
# e.details()


# task 6









# def greeet():
#     print("hello ,  world!")


# def wrapper():
    

# first-task

# def deco(func):
#     def wrapper():
#         print("before function")
#         func()
#     return wrapper
    
# @deco
# def task1():
#     print("task1 is exectuted")

# task1()

# second-task

# def deco(func):
#     def wrapper():
#         print("before function")
#         func()
#         print("after function")
#     return wrapper

# @deco
# def task2():
#     print("task2 is exectuted")

# task2()

# tird-task

# def deco(func):
#     def wrapper():
#         print("before function")
#         func()
#         print("after function")
#     return wrapper

# @deco
# def say_hello():
#     print("hello world")

# say_hello()

# # 4 -task

# def deco(func):
#     def wrapper(*args , **kwargs):
#         print("before function")
#         func(*args , **kwargs)
#         print("after function")
#     return wrapper

# @deco
# def task4(a , b):
#     print(a, b)

# task4(5, 10)


# 5 -task

# def deco(func):
#     def wrapper(*args , **kwargs):
#         print("before function")
#         func(*args , **kwargs)
#         print("after function")
#     return wrapper

# @deco
# def task5(a , b):
#     print(a +b)

# task5(5, 10)


# 6 -task

# def deco(func):
#     def wrapper(*args , **kwargs):
#         result = func(*args , **kwargs)
#         return result
#     return wrapper

# @deco
# def taskmultiply(a , b):
#     print(a  * b)

# taskmultiply(5, 10)




# 7 -task

# def deco1(func):
#     def wrapper():
#         print("decorator 1")
#         func()
#     return wrapper
# def deco2(func):
#     def wrapper():
#         print("decorator 2")
#         func()
#     return wrapper

# @deco1
# @deco2
# def greet():
#     print("hello")

# greet()

# 8 -task

# def deco(n):
#     def 






# @staticmethod

# class Test:
#     @staticmethod
#     def add(a , b):
#         return a+b

# print(Test.add(5,3))


class Company:
    company_name = "TechCorp" #class Variable


    @classmethod
    def change_comapny(cls , new_name):
        return cls.company_name = new_name

company.chnage_company("newTech")
print(comy)