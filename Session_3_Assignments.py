#      ASSIGNMENT- 1

class Student:
    def __init__(self, name , age):
        self.name= name
        self.age=age

    def display(self):
        print(self.name)
        print(self.age)

# # task 1

s1 = Student("Deekshith",21)
s2 = Student("Naveen",22)
print(s1.name , s2.age)
print(s2.name , s2.age)


#  # task 2

s1.display()

# # task 3

class Rectangle:
    def __init__(self , lenght , width):
        self.lenght =lenght
        self.width = width

    def area(self):
        return self.lenght * self.width
    
areaOfRectange = Rectangle(10 , 5)
print(areaOfRectange.area())


# #   task 4

class car:
    def __init__(self , brand , price):
        self.brand = brand
        self.price = price

    def display_details(self):
        print(self.brand)
        print(self.price)

carDetails = car("BMW" , 2500000)
print(carDetails.display_details())


# #   task 5

class Employee:
    def __init__(self , name , salary):
        self.name =name
        self.salary = salary
    def details(self):
        print(self.name)
        print(self.salary)

e = Employee("Deekshith" , 25000)
e.details()


# task 6






    

# first-task

def deco(func):
    def wrapper():
        print("before function")
        func()
    return wrapper
    
@deco
def task1():
    print("task1 is exectuted")

task1()

# second-task

def deco(func):
    def wrapper():
        print("before function")
        func()
        print("after function")
    return wrapper

@deco
def task2():
    print("task2 is exectuted")

task2()

# tird-task

def deco(func):
    def wrapper():
        print("before function")
        func()
        print("after function")
    return wrapper

@deco
def say_hello():
    print("hello world")

say_hello()

 # 4 -task

def deco(func):
    def wrapper(*args , **kwargs):
        print("before function")
        func(*args , **kwargs)
        print("after function")
    return wrapper

@deco
def task4(a , b):
    print(a, b)

task4(5, 10)


# 5 -task

def deco(func):
    def wrapper(*args , **kwargs):
        print("before function")
        func(*args , **kwargs)
        print("after function")
    return wrapper

@deco
def task5(a , b):
    print(a +b)

task5(5, 10)


# 6 -task

def deco(func):
    def wrapper(*args , **kwargs):
        result = func(*args , **kwargs)
        return result
    return wrapper

@deco
def taskmultiply(a , b):
    print(a  * b)

taskmultiply(5, 10)




# 7 -task

def deco1(func):
    def wrapper():
        print("decorator 1")
        func()
    return wrapper
def deco2(func):
    def wrapper():
        print("decorator 2")
        func()
    return wrapper

@deco1
@deco2
def greet():
    print("hello")

greet()

# 8 -task

def deco(n):
    def 








# Last - Assignment

 # task 1 and 2

class Employee:
    company = "Techcorp"
    def __init__(self , name , salary):
        self.name = name
        self.__salary = salary

    def display(self):
        print(self.name)
        print(self.__salary)
        print(self.Employee.company)

@classmethod

#task 3

class Person:
    def __init__(self , name):
        self._name=name


 # task 5

@staticmethod
def is_valid_salary(salary):
    return salary>0


# #task 6

@staticmethod
def greet_comapny():
    print(Employee.company)


# #task 7

@property
def salary(self):
    return self.__salary

# #task 8

@property
def annaual_salary(self):
    return self.__salary *12

# # task 9

e1 = Employee("deeekshith" , 20000)
e2 = Employee("naveen" , 25000)
e3 = Employee("maruthi" , 19000)

Employee.change_comapny("Wipro")

print(e1.name , e1.salary)
print(e2.name , e2.salary)
print(e3.name , e3.salary)
