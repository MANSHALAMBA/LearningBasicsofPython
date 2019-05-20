#why is file system so important ?
#sometimes 

# opening file first 
#u have to open first the file to work with it
# u also have to specify acess mode while opening by default that is read mode
#also remeber that open wonactually physically open a file, like poping up of new window like of word files that wont happen

file="demo.txt"
accessmode="w"
 
 # all do the same thing
workinfile=open(file,accessmode)
workinfile=open(file,mode="w")
workinfile=open(file,mode=accessmode)
workinfile=open("demo.txt",mode="w")
workinfile=open("demo.txt","w")
# acessmode is a i.e append
workinfile=open("demo.txt","a")

#BIG DIFFERENCE : when u open a file in write mode it overwrites the contents of file then opens but 
                  #in append mode it doesnot overwrites just opens it .!!!




#REMEMBER: by default file directory is homedirectory->documents
           # if file is not present there then new one will be created.




# write function #unpredictable output  
workinfile.write("I started writing")
workinfile.write("I again wrote in same line\n")
workinfile.write("I wrote in new line yayayayaya")



#reading from files #caution: u cant read files when u open it in write mode
workinfile=open("demo.txt","r")
filecontent=workinfile.read()
print(filecontent) #prints exactly in same format as in file
#in another session 
content=workinfile.readline()
print(content)
#Great concept the below segment will automatically print the 2nd line.
content=workinfile.readline()
print(content)

#if you have executed line umber 42 in one session then in same session output of readline() will be be blank .

#observe op
filecontent=workinfile.read()
print(filecontent)

# in nutshell in one session pointer is maintained on file which depicts till where it has been read. 

#specific function for reading csv files.
import csv
# below will run at once in interpreter coz its a unit of code.
with open("demo.txt","r") as myfile: # another way of opening file difference it automaticlaay closes file after coming out of indentation or if any error takes place.
      content=csv.reader(myfile) #reader is a function for reading csv files by default separator chharacter is , 
#content is a list of lists jiski one value depicts an row of csv file
    #   for rows in content:
    #       print(rows)
    #       for a in rows:
    #           print(a)      
#neater of printing string lists of above commented code
      for rows in content:
          print(','.join(rows))
          for a in rows:
               print(a)  