# # slicing

nums =[10,20,30,40]
print(nums[])

nums =[10,20,30,40]
print(nums)

s = 'DataScienceIsAwesome12345'
first = s[4:11]
print(first)

third = s[::2]
print(third)

fourth = s[:-5]
print(fourth)

second = s[0:13] + s[13:20][::-1] + s[20:25]
print(second)

fifth = s[0:4][::-1] + s[4:21] + s[21:25][::-1]
print(fifth)


name = input("enter the student name: ")
age = int(input("enter age: "))
marks = list(map(int , input('enter marks: ').split()))
subjects = input('enter subjects: ').split()



total = sum(marks)
average = total/len(marks)

if average >= 75:
    result = "Distinction"
elif average >= 50 and average < 75:
    result = 'pass'
else:
    result = 'fail'

print(total)
print(average)
print(result)


a = 5
b= 3
print( a & b)
print( a | b)
print( a ^ b)
print( a << 1)
print( a >> 1)













