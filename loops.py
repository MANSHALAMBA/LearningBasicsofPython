#drawing tool in python
import turtle
turtle.forward(100)
# another window called python graphics pop up to display output
  # if we close that window u need run turtle.Terminator this command after closing window and then go forward.


#making letter M 
turtle.color('red')
turtle.forward(70)
turtle.right(135)
turtle.forward(35)
turtle.forward(35)
turtle.backward(35)
turtle.forward(35)
turtle.left(135)
turtle.forward(70)
turtle.undo()
turtle.forward(45)
turtle.undo()
turtle.right(45)
turtle.forward(70)
turtle.forward(15)
turtle.forward(5)
turtle.right(135)
turtle.forward(70)

#drawing circle
turtle.circle(50)

 #returns turtle's speed
turtle.speed()

# u can even set turtle's speed
turtle.speed(8)
turtle.forward(50)

# for more vist docs , there are many more functions


# FOR LOOPS # making square using foor loop
for anyname in range(4):
    turtle.forward(100)
    turtle.right(90)


#nested for loops
for anyname in range(4):
        turtle.forward(10)
        turtle.right(90)
        for steps in range(4): # this loop will execute 4*4=16 times.
           turtle.forward(50)
           turtle.right(90)

#cute!!!!! figure
for anyname in range(4):
    turtle.forward(100)
    turtle.right(90)
    for steps in range(3):
        turtle.circle(5)
#for is really not necessary in above code it will just draw circle 3 times on first circle again and again.
# same cute figure
for anyname in range(4):
    turtle.forward(100)
    turtle.right(90)
    turtle.circle(5)   


# variables in loop and turtle commands
nbrsides=4
for anyname in range(nbrsides):
        turtle.forward(100)
        turtle.right(360/nbrsides)
        for steps in range(nbrsides):
           turtle.forward(50)
           turtle.right(360/nbrsides)


# acessing the loop value.
 # here steps is the loop value.
for steps in range(5):
    print(steps)
# here i tried to start steps from 1 
  # but it didnt work.
steps=1
for steps in range(5):
    print(steps)

# the CORRECT WAY IS!!
for steps in range(1,5): # instead of running 5 times it will run 4times coz we started from 1
    print(steps)


#step size in for loop , 

for steps in range(5,2): # no output
  print(steps)

 #for using step size u ought to use a start index.
for steps in range(0,5,2):
  print(steps)

for steps in range(1,5,2):
  print(steps)


# eqquivi of foreach loop in python

for steps in [20,14,2,0]:
    print(steps)

for color in ['red','blue', 'green' , 'yellow']:
    turtle.color(color)
    turtle.forward(20)
    turtle.right(90)

for color in ['red','blue', 'green' , 5]: #code will crash 5 is not acceptable arg to color
    turtle.color(color)
    turtle.forward(20)
    turtle.right(90)


#but u can mix datatypes

for color in ['red','blue', 'green' , 5]: 
    print(color)


