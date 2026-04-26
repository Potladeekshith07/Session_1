print('hello world')
name='newone' #string
age=20 #integer
height=5.9 #float
is_student=True #boolean
na=None #null value

'''operators
arithmetic operators: +, -, *, /, %, **, //
comparison operators: ==, !=, >, <, >=, <=
logical operators: and, or, not
assignment operators: =, +=, -=, *=, /=, %=, **=, //
bitwise operators: &, |, ^, ~, <<, >>'''

a=10
b=3
print(a+b) #addition
print(a-b) #subtraction
print(a*b) #multiplication
print(a/b) #division
print(a%b) #modulus
print(a**b) #exponentiation
print(a//b) #floor division
x=5
x+=2 #x = x + 2
print(x)
x*=3 #x = x * 3
print(x)
x-=4 #x = x - 4
print(x)
x/=2 #x = x / 2
print(x)
a,b=5,10 #multiple assignment
print(a)
print(b)
# comparision operators
print(a==b) #equal to
print(a!=b) #not equal to
print(a> b) #greater than
print(a< b) #less than
print(a>=b) #greater than or equal to
print(a<=b) #less than or equal to
# logical operators
print(a>3 and b>15) #logical and
print(a>3 or b>15)
print(not(a>3 and b>15)) #logical not
a=5
b=10
print(a & b) #bitwise AND
print(a | b) #bitwise OR
print(a ^ b) #bitwise XOR
print(~a) #bitwise NOT
print(a << 1) #left shift
print(a >> 1) #right shift
# membership operators
text='hello world'
print('hello' not in text) #membership operator
# identity operators
a=[1,2]
b=[1,2]
print(a is b) #identity operator
print(a==b) #equality operator
#MUTABLE DATA TYPES: LIST ,SET ,DICTIONARY
apples=['red','green','yellow','yellow',[1,2,3]] #list-index base
# IMUTABLE DATA TYPE:TUPLE ,
appl=('red','green','yellow','yellow',[1,2,3]) #tuple-ordered,
unchangeable, allows duplicate values
# appl.append('blue') #adding an element to the list
'''appl.append('blue') #adding an element to the tuple will raise an
error
print(appl)
'''
apples.append('blue')
print(apples)
fruits={'apple':'red','banana':'yellow','orange':['reds','oranges']}
#dictionary
# set- unordered, unindexed, no duplicate values
fruit_set={'apple','banana','orange','apple'} #set
print(fruit_set) #will not include duplicate 'apple'
fruit_set.append('blue')