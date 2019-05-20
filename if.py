
a="yes"
if a=="yes" :           
    print("hey hey")
print("have a nice day")

if a=="yes" :print("hey hey") #this is also correct


if  a=="YES": print("wo wo ") #python is case sensitive

if a.upper()=="YES": print(" wo wo ") 

b="11pm"
if not b=="11pm": print("STUDY") #kinda opposite of if statement.

deposit=input("how much do u wannna deposit?")
# you can't compare strint to numeric values , but can compare int and float
if int(deposit)>100: print("you get free toaster") 

if float(deposit)>100: print("you get free toaster")


#elif statements , elif a short form for else if

favplayer=input("HEY THERE ENTER YOUR FAVOURITE CRICKET PLAYER").upper()
   #conditions will be checked from top to bottom once a condition matches further conditions and else wont be executed
if favplayer=="VIRAT KOHLI":
    print("Virat Rocks !!!")
elif favplayer=="SACHIN TENDULKAR":
    print("Sachin Sir is Real Hero")
elif favplayer=="":          #here note that this is the case when user enters nothing.
     print("NO favourites")
else :print("Sorry No tag for your favourite")
else favplayer=="TRIAL":print("Sorry No tag for your favourite") #synatxerror u cant have condition in else

# and or , logic exactly same as and , or gate respectively.

day=input("ENTER THE DAY").upper()
venue=input("ENTER THE VENUE").upper()

if day=="SUNDAY" or venue=="NSP":
    print("YEAH am coming")
elif day=="HOLIDAY" and venue=="ICESKATING":
    print("YEAH am coming")
else : print("Am not interested ")

# using and,or togeather in a statement
# precendence of and is greater so it will execute first
a=4
b=11
if a>5 and b>5 or b>10:   #will execute
    print("am executing") 

a=4
b=9
if a>5 and b>5 or b>10:    #wont execute
    print("am executing") 

#but remember parenthesis always have greater priority
a=4
b=1
if a>5 and (b>10 or b<2):  #wont execute
    print("am executing")


#nested statements
day=input("enter the day").upper()
sleepy=input("true if u r sleepy else false").upper()
if day=="MONDAY":
    print("hey NEW WEEK")
    if sleepy=="TRUE":
        print("sleep")
    print("have a great week ahead")








