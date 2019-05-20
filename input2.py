a=input("whta is \nur name ?\n") #here u can see that within quotes it is just a string like it used to be in within print
                                #difference that in addition to printing it also returns input from user.
print(a)

FirstName=input("what is your first name")

LastName=input("what is your last name")

# input returns string type

print("the full name is " + FirstName + " " + LastName) # concatenation of variable with string

# srting functions : lower, upper , capitalize , swapcase , replace , find , count

string="ol ol "

string.count("o")

string.count(" ") # this is so amazing dhyan se dekh name of variable is different but still working well

string.count("ol") 

string.count("o l") # returns 0 
number=input("i need number")

print(number)
 number.count('2') # input always returns string

 a=2**3
 print(a)

 #calculating area

 height=100
 width=200

 area=width*height/2
 print(area)

 print("the area is " + area) # only a string can be concatenated to a string

 print( " the area is %d " %area) # correct way , d means integer a place holder here
print( " the area is %f " %area)
print( " the area is %.2f " %area)
print("the area is {0:.2f} " .format(area)) # another way of doing above thing
print("the area is { 0:.2f} " .format(area)) # error bcoz of space
    #on running these examples you will get to know the number u specify before d is  totalwidth for output .an dif u specify 0 then 0 gets printed in place of space but totalwidth is maintained.
print("formatting decimal number %12d" %6)
print("formatting decimal number %02d" %6)
print("formatting decimal number %d" %6)
print("formatting decimal number %2d" %6)
print("formatting decimal number %002d" %6)

# multiple number output
print(" first number is %d second number is %f " %2 %3.0) #error
print("the first number is {0:.2f} and second number is {1:d} " .format(1.1 , 2)) #noerror

#imp example 
print(" some numbers {0:d}" .format(1) + " hey there %d" %32  ) 

salary=input("enter your slary")
bonus=input("enter the bonus")

print( salary + bonus ) # undesireable output !!!
# use inbuilt functions for conversion to require datatype.!!!
salary= int(salary)
bonus =int(bonus)

print(salary+bonus)


int("bob") # error int can't convert obvio this input to integer
