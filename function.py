def my1stfunc():          #definig func
    print("hey there")

my1stfunc()       #calling func

def a():         #no error
    b()

a()            #now u get error coz b

def b():
    print("i was not defined before calling me")

# fully functional use of function
def main():
  names=[]
  for steps in range(5):
      a=input("enter a name")
      names.append(a)
  printlist(names)

def printlist(names):
    print(',' .join(names))

main()


#returning  data from function

# same func working well for different datatypes , POWER OF PYTHONf
def adder(number1,number2):
    return number1+number2

answer=adder(5,10)
print(answer)

answer=adder("hi","mom")
print(answer)


# calling a function within a function call is very much possible.
def func():
    return "a"

def func2(something):
    print(something)

func2(func())  
""
