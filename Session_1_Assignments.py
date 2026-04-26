# TASK 1

name = "John"
age = 20
height = 5.9
is_student = True
extra_info = None

print( name)
print(age)
print(height)
print(is_student)
print(extra_info)


# Task 2

a = 10
b = 5

print( a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)


#task 3

score = 50
print(score)

score += 10
print( score)

score -= 5
print(score)

score *= 2
print(score)

score /= 5
print(score)



# task 4


std_1 = 20
std_2 = 18
score = 60

print(std_1 == std_2)
print(std_1 != std_2)
print(std_1 > std_2)
print(std_1 < std_2)
print(std_1 >= std_2)
print(std_1 <= std_2)
print(std_1 > 18 and score > 40)

#task - 5


x = 5
y = 10

print( x & y)
print(x | y)
print(x ^ y)
print(~x)
print(x << 1)
print(y >> 1)

#task - 6

text = "python programming"
print("python" in text)

lst1 = [1, 2, 3]
lst2 = [1, 2, 3]

print(lst1 is lst2)
print(lst1 == lst2)


# task - 7


#List

subjects = ["Math", "Science", "English", "Math", ["Python", "Java"]]
subjects.append("History")
print("List:", subjects)

# Tuple

tup = ("Math", "Science", "English")
print("Tuple:", tup)
# tup[0] = "Physics"   # Error because tuple is immutable

# Dictionary

student = {
    "name": "John",
    "marks": {"math": 80, "science": 75},
    "subjects": subjects
}
print("Dictionary:", student)



# Set

sub_set = {"Math", "Science", "English", "Math"}
print("Set:", sub_set)


#task - 8

total = student["marks"]["math"] + student["marks"]["science"]
average = total / 2

if average >= 75:
    result = "Distintion"
elif average >= 50:
    result = "Pass"
else:
    result = "Fail"

print("Total:", total)
print("Average:", average)
print("Result:", result)