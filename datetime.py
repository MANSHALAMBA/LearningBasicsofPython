import datetime  # even if u are working through interpreter u need to run this command
a=datetime.date.today()


print(a)
print(a.year)
print(a.month)
print(a.day)
  # like there are functions for conversion fromone datatypr to another here we have another function for formatting dates
a.strftime('%d %b %y')
a.strftime('%d %b , %Y')
a.strftime(" today's date is %d %b %Y")
# birthday calculator #here format needs to be exactly matching even the separators   
userinput=input("hey enter your birthday mm/dd/yyy ")


birthday=datetime.datetime.strptime(userinput,'%m/%d/%y') #error u enter 4 digit year that wont match with %y

birthday=datetime.datetime.strptime(userinput,'%m/%d/%Y')

   #run these
userinput=input("hey enter your birthday mm/dd/yy ")

birthday=datetime.datetime.strptime(userinput,'%m/%d/%y')
birthday=datetime.datetime.strptime(userinput,'%m/%d/%y').date() # date() to just print date no time
currentdate=date.date.today()
# currentdate=date.datetime.today()
noofdaysleft=currentdate-birthday  # this is so great u can subtract dates , 

print(noofdaysleft.days)
print(noofdaysleft)
    # thing to note is u can even include time for that exclude 25th line and include 27 instead of26







