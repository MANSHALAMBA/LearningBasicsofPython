# try except in python for dealing with run time error

#simple division calc
import sys
firstnumber=float(input("first number"))
secondnumber=float(input("second number"))

answer=firstnumber/secondnumber

print(answer)

# hadling the error division with 0 not allowed
# in try block immediately when an error is detected control moves to except block.
try:
    a="hey"
    answer=firstnumber/secondnumber
    print(answer)
except ZeroDivisionError:  # if u know the exact error to be occured.
       print("dividing by zero is an error for computer but the answer is infinity.")
except: # except should be last after all specific excepts.
    print("some error encoutered in try block ")
    error=sys.exc_info()[0] # gives precise info about error occured
    print(error)
finally:  #ususally used for closinf files or databases.
    print("This blocks executes no matter except block runs or try block")

 print(a)# will always give hey no matter exception occurs or not   

# we can even use sys.exit() to exit program i.e no statement after it will execute but even in case of sys.exit() finally still executes. 