
# # Assignment - 1


# # 1

# num = int(input("enter a number: "))
# if num%2==0:
#     print("even")
# else:
#     print("odd")

# # 2

# a = int(input("enter 1st number : "))
# b = int(input("enter 2nd number : "))
# c = int(input("enter 3rd number : "))
# if a>=b and a>=c:
#     print(a)
# elif b>=a and b>=c:
#     print(b)
# else:
#     print(c)

# # 3

#     marks=int(input("enter your marks : "))
# if marks >= 75:
#     print("distinction")
# elif marks>=50 and marks<75:
#     print("pass")
# else:
#     print("fail")

# # 4


# for i in range(1 , 11):
#     print(i)


# # 5


# number = int(input("enter number : "))
# sum = 0
# i=1

# while i<=number:
#     sum+=i
#     print(sum)


# # 6


# for i in range (1,21):
#     if i%3==0:
#         continue
#     print(i)


# # 7

# nums = [5,10,15,-2,20]

# for n in nums:
#     if i<0:
#         break
#     print(num)


# # 8


# number = int(input("enter number : "))
# for i in range(1,11):
#     print(number * i)

# # 9

# number = int(input("enter number : "))
# if number>1:
#     prime =True

#     for i in range(2,number):
#         if num%i==0:
#             prime = False
#             break
#         if prime :
#             print("yeah it a prime")
#         else:
#             print("its not a prime")
# else:
#     print("its not a prime")


# # 10

# for i in range(1,6):
#     for j in range(i):
#         print("*", end="")
#     print()




#     # Assignment - 2


# # 1


# def welcome():
#     print("Welcome to python")
# welcome()

# # 2

# marks = [80,70,90]
# def get_total(marks):
#     return sum(marks)
# print(get_total(marks))


# # 3


# def greet(name="Guest"):
#     return f"hello {name}"
# print(greet())
# print(greet("Abhi"))

# # 4


# def calculator(marks):
#     total = sum(marks)
#     avg = total / len(marks)
#     return total , avg

# total , avg = calculator(marks)
# print(total)
# print(avg)

# # 5

# def total_marks(*marks):
#     return sum(marks)

# print(total_marks(80,80,90))

# # 6

# def student_info(**data):
#     return data
# print(student_info(name="deekshith",age=21,course="python"))

# # 7

# square = lambda x:x*x
# for i in marks:
#     print(square(i))

# # 8


# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))


# # 9

# def modify_list(list):
#     list.append(100)

# numbers = [10,20,30]
# modify_list(numbers)
# print(numbers)

# # 10

# def modify_num(x):
#     x=x+10
#     return x
# num = 5
# new_num = modify_num(num)
# print(num)
# print(new_num)


# # 11

# name = input("enter name : ")
# marks = list(map(int , input("enter marks : ").split()))
# print(name)
# print(marks)

# import math
# print(math.sqrt(100))

# # 12

# import math
# total = 225
# print(math.sqrt(total))


# # 13

# def get_result(avg):
#     if avg >= 27:
#         return "Distinction"
#     elif avg >= 50:
#         return "pass"
#     else:
#         return "Fail"
    
# avg = 78
# print(get_result(avg))


# # 14

# name = input("student name :")
# m1 = int(input("mark1: "))
# m2 = int(input("mark2: "))
# m3 = int(input("mark3: "))

# marks = [m1,m2,m3]

# def get_total(marks):
#     return sum(marks)

# def get_average(total):
#     return total / len(marks)

# total = get_total(marks)
# avg = get_average(total)
# result = get_result(avg)

# bonus = list(map(lambda x: x+5 , marks))

# def fact(n):
#     if n==1:
#         return 1
#     return n* fact(n-1)


# lst = [1,2]
# lst.append(3)

# print("name : " , name)
# print("marks : " , marks)
# print("total : " , total)
# print("average : " , avg)
# print("result : " , result)
# print("bonus : " , bonus)
# print("factorial of 5 : " , fact(5))
# print("square root of total : " , math.sqrt(total))
# print("mutable list : " , lst)


# Assignment - 3


#  1st task
n = int(input("number of student : "))
students = []


# 2nd task

for i in range (n):
    print("enter details of student {i+1}")
    name = input("student name : ")
    age = int(input("student age : "))
    marks = list(map(int , input("enter marks : ").split()))
    subjects = input("enter subjects : ").split()

    student = {
        "name" : name , 
        "age" : age ,
        "marks": marks,
        "subjects" : subjects
    }

students.append(student)


# task 3

for student in students:
    subjects_tuple = tuple(student["subjects"])
    unique_subjects = set(student["subjects"])

# task 4

for student in students:
    student["subjects_tuple"] = tuple(student["subjects"])
    student["unique_subjects"] = set(student["subjects"])


# task 5

for student in students:
    marks = student["marks"]
    
    student["first2"] = marks[:2]
    student["last2"] = marks[-2:]
    student["reverse"] = marks[::-1]
    student["step2"] = marks[::2]


    
# task 6

for student in students:
    marks = student["marks"]
    
    student["total"] = sum(marks)
    student["average"] = sum(marks) / len(marks)
    student["highest"] = max(marks)
    student["lowest"] = min(marks)




# task 7

for student in students:
    avg = student["average"]
    
    if avg >= 75:
        student["result"] = "Distinction"
    elif avg >= 50:
        student["result"] = "Pass"
    else:
        student["result"] = "Fail"




# task 8

for student in students:
    age = student["age"]
    total = student["total"]
    
    student["bit_and"] = age & total
    student["bit_or"] = age | total
    student["bit_xor"] = age ^ total





# task 9

def total(marks):
    return sum(marks)

def average(marks):
    return sum(marks) / len(marks)

def result(avg):
    if avg >= 75:
        return "Distinction"
    elif avg >= 50:
        return "Pass"
    else:
        return "Fail"



# task 10

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("deekshith")



# task 11

def total_marks(*args):
    return sum(args)

print("Total using *args:", total_marks(90, 80, 70))



# task 12

def student_profile(**kwargs):
    return kwargs

print(student_profile(name="Abhi", age=22, city="Chennai"))


# task 13

for student in students:
    student["square_marks"] = list(map(lambda x: x*x, student["marks"]))

students.sort(key=lambda x: x["average"], reverse=True)




# task 14

def apply_function(func, values):
    return list(map(func, values))

print(apply_function(lambda x: x+5, [1,2,3]))



# task 15

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

for student in students:
    student["factorial_subjects"] = factorial(len(student["subjects"]))





# task 12



# task 12


# task 12