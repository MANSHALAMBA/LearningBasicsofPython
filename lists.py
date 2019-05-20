#lists is used to store multiple values
#can store multiple values of different datatypes in a single lists
# but is is  recommended to have a single datatype in 1 lists

a=[] #empty lists

names=['mansha','kammo','nisha','sanvi']

#indexing starts with 0 from aage
print(names[0])

#indexing from backwards starts with -1 then -2 and so on.
print(names[-1])

print(names[-2])

#updating lists value
names[0]='manshalamba'

#append function
names.append('sushie')
print(names[-1])

#remove function 

names.remove('manshalamba')#it takes a value not a index.# it will only remove first value found.
#there will be no void all values wil move 1 forward.
print(names[0])#so now kammo is on 0 index.

# another way to do above is using del
del names[0]
print(names[0])#now nisha is on 0 index

#searching in lists
print(names)
names.index('sanvi')
names.index('sanya') #since sanya is not in list , it will give an error


#loops and lists
fruits=["apple", "orange","pear", "strawberrry"]

for steps in range(4):
    print(fruits[steps])


#using len function

for steps in range(len(fruits)):  #same output as in line 43
    print(fruits[steps])

#equiv of for each loop
for steps in fruits:
    print(steps)

#also the above loop is dynamic coz 
#if we append something in fruits list inside for loop 
#then loop will also that appended entries
#example :

for steps in fruits:           #infinite loop
    fruits.append("lichi")
    print(steps)
#sort method in lists
fruits.append("guvava")
fruits.sort()
fruits #sorted lists

numbers=[10,6,11]
numbers.sort() # sort method in numbers gives ascending order. 




