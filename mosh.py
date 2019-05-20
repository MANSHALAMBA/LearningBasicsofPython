print("hello ")

print("hi" * 4)

# this is too cool ,the string will be printed 4 times , in other languages we had to do nasty loops for this
print("hi \n" * 4)


x=1
y=2
# equivalent to line number 9 and 10
x,y = 1,2

print(y)
#type used to determine type , in pyhton we have like this class int , class bool so basically all ints are instances of class int and similarly for other datatypes
print(type(x))

# pyhton is dynamically typed datatypes are deceided on runtime.
# u can very well do  no error will be given.
a=20
a="a string variable"

# python version 3.6 comes with type annotattion.

# .............
# id inbuilt function that returns adress of an variable
print(id(a))

# in python all built in data types are immutable.
#example is as follows
x=1
print(id(x))
x=x+1
print(id(x)) #op will be different from line no. 32 , coz we stopped refrencing to previous memory location python's automatic memory management will release that memory location.

# same thing in elements of lists
x=[0,1,2]
print(id(x[0]))
x[0]=3
print(id(x[0]))

# but remember 
print(id(x))
x.append(4)
print(id(x))

# string in python
string="Python programming"
print(len(string))
print(string[0])
print(string[-1])
print(string[0:3]) #print substring
print(string[:3])
print(string[0:])
print(string[:])
num=5
b=f"{string} {num}" # b is evaluated at runtime.
print(b)
print(type(b))
print(type(num))

x=0b10       #0b specifies binary format
print(x)     #output 10
print(bin(x))  #op binary format of specified number

x=0x12c        #0x specifies hexadecimal format 
print(x)      #output 300
print(hex(x))   #op hexadecimal format of specified  number

#complex numbers 
x=1+2j   # or x=1+2J
print(x)

# different arithematic operators in python
#increment and decrement operators not their in python
x=10//3  # give quotient in int type
print(x)

x=2**3  # raise to the power
print(x)

#working with numbers
PI=3.14 # in pyhton there are no constants developers use capital convention to represent constant numbers.

print(round(PI)) #op 3
PI=-3.14
print(abs(PI)) #op 3.14


# for more functionality of maths use import math module.
import math
print(math.factorial(4)) #op 24 

# in pyhton no implicit type conversion unlike java
# thus python is strongly typed language.

# like javascript there are falsy values -> 0 , "" , [] , null  all values other than these are true in terms of boolean .

# conditionals
if 3<2:
   pass   # if we dont want to perform anything we can't keep blank , we use pass
elif 4>3:
    print("HEY")


name="mohit"

if not name.strip() : # heya will be printed if name is empty , " " is not an empty string for pyhton so by using strip() i ensure ki there is some value in string.
    print("heya")


#chaining comparison operators
age=20
if age>=18 and age<65:
    print("eligible")

#python way of above
if 18<=age<65:
   print("Eligible")

#ternary operator in python
age=15
message="Eligible" if age>=18 else "not eligible"
print(message)

#range objects
for i in range(5):# here range function returns range object which iterable 5 times but takes significantly less space as compared to lists.
    print(i)

print(type(range(5)))
print(range(5))


#for else loop
names=['mansha' , 'mohit' , 'madhu' , 'naresh' , 'Jony']
for name in names:
    if name.startswith("J"):
        print("found")
        break
else: print("not found") #this will execute when break wont be executed 

# default values of args , tuple 
def increment(number, by=1):
    return(number , number+by)  #retruning tuple.
print(increment(2,3))
print(increment(2))
print(increment(2.5))

# *before any parameter converts it into list
def function(*a):
    for i in a:
        i=i+1
        print(i)

function(1,2,3,4,5) # attetion here I didnt pass a list

# **befrore any parameter converts it into dictionary

def function2(**user):
    print(user["name"])

function2(id=1,name="admin")

# there global scope and func scope  no if scope.
message="a"
def func():
    global message # to acess message of global scope , this IS  BAD PROGRMMING PRACTICE.[ EDITING GLOBAL VARIABLE IN LOCAL SCOPE]
    message="b" # this will create new variable of local scope , this is good programming practice.

func()
print(message) #this will print a



          




