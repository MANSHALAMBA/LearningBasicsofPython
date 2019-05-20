# while loop is used when developer does not know how many times the loop will run
# relate while to english wala while like jab tak condition true hai tab tak loop runs. 

answer='0'

while answer!='4':
    answer=input("what is 2+2=?")

# drawing square using while loop.
import turtle
counter=0
while counter<4:
 turtle.forward(100)
 turtle.right(90)
 counter=counter+1 # extra work to be done in comparison to for loop 
    
    ye wala while loop will run 5 times , so u have to be aware how many times while loop will run. that is why it is better to make a personal convention like mine will be to always start while loop with 0 & use < in condition.
#  while counter<=4:     
#  turtle.forward(100)
#  turtle.right(90)
#  counter=counter+1 

#incrementing in python
++a #no increment
a++ #no increment

a+=1 # will work awesome.!!!

