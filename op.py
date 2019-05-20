Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> workinfile=open("demo.txt","r")

>>> content=workinfile.readline()
>>> print(content)

me,20

>>> content=workinfile.readline()
print(content)

SyntaxError: multiple statements found while compiling a single statement
>>> content=workinfile.readline()
>>> print(content)
bhai,24

>>> filecontent=workinfile.read()
>>> print(filecontent)
mom,50
dad,55
>>> import csv
>>> with open("demo.txt","r") as myfile:
      content=csv.reader(myfile)

   for rows in content:
       print(row)       

SyntaxError: unindent does not match any outer indentation level
>>> with open("demo.txt","r") as myfile:
      content=csv.reader(myfile)

      for rows in content:
          print(row)

          
Traceback (most recent call last):
  File "<pyshell#11>", line 5, in <module>
    print(row)
NameError: name 'row' is not defined
>>> with open("demo.txt","r") as myfile:
      content=csv.reader(myfile)

      for rows in content:
          print(rows)

          
['me 20', '']
['bhai 24', '']
['mom 50', '']
['dad 55', '']
>>> with open("demo.txt","r") as myfile: # another way of opening file difference it automaticlaay closes file after coming out of indentation or if any error takes place.
      content=csv.reader(myfile) #reader is a function for reading csv files by default separator chharacter is , 
#content is a list jiski one value depicts an row of csv file
      for rows in content:
          print(rows)

          
['me', '20']
['bhai', ' 24']
['mom', ' 50']
['dad', ' 55']
>>> with open("demo.txt","r") as myfile: # another way of opening file difference it automaticlaay closes file after coming out of indentation or if any error takes place.
      content=csv.reader(myfile) #reader is a function for reading csv files by default separator chharacter is , 
#content is a list of lists jiski one value depicts an row of csv file
      for rows in content:
          print(rows)
          for a in rows:
              print(a)

              
['me', '20']
me
20
['bhai', ' 24']
bhai
 24
['mom', ' 50']
mom
 50
['dad', ' 55']
dad
 55
>>> a=[1,2,3,4]
>>> print(a)
[1, 2, 3, 4]
>>> print(':'.join(a))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(':'.join(a))
TypeError: sequence item 0: expected str instance, int found
>>> a=["a","b","c"]
>>> print(a)
['a', 'b', 'c']
>>> print(':'.join(a))
a:b:c
>>> for rows in content:
          print(','.join(rows))
          for a in rows:
              print(a)

              
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    for rows in content:
ValueError: I/O operation on closed file.
>>> for rows in content:
          print(','.join(rows))
            for a in rows:
               print(a)
               
SyntaxError: unexpected indent
>>> for rows in content:
          print(','.join(rows))
          for a in rows:
               print(a)

               
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    for rows in content:
ValueError: I/O operation on closed file.
>>> with open("demo.txt","r") as myfile: # another way of opening file difference it automaticlaay closes file after coming out of indentation or if any error takes place.
      content=csv.reader(myfile) #reader is a function for reading csv files by default separator chharacter is , 
#content is a list of lists jiski one value depicts an row of csv file
      for rows in content:
          print(rows)
          for a in rows:
              print(a)      
#neater of printing string lists
      for rows in content:
          print(','.join(rows))
          for a in rows:
               print(a)

               
['me', '20']
me
20
['bhai', ' 24']
bhai
 24
['mom', ' 50']
mom
 50
['dad', ' 55']
dad
 55
>>> with open("demo.txt","r") as myfile: # another way of opening file difference it automaticlaay closes file after coming out of indentation or if any error takes place.
      content=csv.reader(myfile) #reader is a function for reading csv files by default separator chharacter is , 
#content is a list of lists jiski one value depicts an row of csv file
    #   for rows in content:
    #       print(rows)
    #       for a in rows:
    #           print(a)      
#neater of printing string lists
      for rows in content:
          print(','.join(rows))
          for a in rows:
               print(a)

               
me,20
me
20
bhai, 24
bhai
 24
mom, 50
mom
 50
dad, 55
dad
 55
>>> 
