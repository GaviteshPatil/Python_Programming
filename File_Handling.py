 #Below the progamming tips 

#Programming Tip:- Folder names and file names case sensitive in Windows but they are case insensitive in Linux.

#Note:- The characters after the dot form the extension of the fil. For example .docx indicates that the file is a word document.

#Note :- A relative path is specified relative to the program's current working directory.

#Note :- If you use a relative file path from the wrong directory, then either the wrong file will be accessed or no file will be accessed if no file of the specified name exits in the given path.

#Programming tip:- The contents of a binary file are not human readable . If you want that data stored in the file must be human-readable, then store the data in a test file.

#Note : - In a text file, each line of data ends with a newline character. Each file ends with a special character called the end-of-file (EOF) marker.

#Note :- Binary files store data in the internal representation format. Therefor, an integer value will be stored in binary form aas 2 byte value. the same format is used to store data in memory as well as in file. Like text file , binary file also ends with an EOF market.

#Note :- Binary files are mainly used to store data beyound text such as images, executables, etc.

#Programming knowledge:- To open the file we use the built-in open() function. 
"""This function creates a file object, which will be used to invoke methods associated with it. """

#syntax:- "fileObj = open(file_name [, access_mode])"

#file_name is a string value that specifies name of the file that you want to access. 
#access_ mode indicates the mode in which the file has to be opened , i.e., read , write , append , etc.
#The open() funtion returns a file object .


#program to demonstrete the open() fucntion in the file handling
file=open("file_handling.txt","rb")
print(file)

#Note:- Access mode is an optional parameter and the default file access mode is read(r).

#Access Modes .
"""  r :- This is the default mode of opening a file which opens the file for reading only.
          The file pointer is placed at the beginning of the file."""

"""  rb :- This mode opens a file for reading only in binary format . 
           The file pointer is placed at the beginning of the file."""

"""  r+ :- This mode opens a file for both reading and writing .
           The file pointer is placed at the beginning of the file."""

"""  rb+ :- This mode opens the file for both reading and writing in binary format.
            The file pointer is placed at the beginning of the file."""

"""  w  :- This mode opens the file for writing only.When a file is opened in w mode, two 
           things can happen. If the file does not exist , a new file is created for writing 
           . If the file already exists and has some data stored in it, the contents are overwritten."""

"""  wb :- Opens a file in binary format for writing only. When a file is opened in this mode, two things can happen . 
         If the file does not exist, a new file is created for writing . If the file already exists and has some data stored in it , the contents are overwritten."""

"""  w+ :- Opens a file for both writing and reading . When a file is opened in this mode, two things can happen . 
         If the file does not exist, a new file is created for writing . If the file already exists and has some data stored in it , the contents are overwritten."""

""" wb+ :- Opens a file in binary format for both reading and writing . When a file is opened in this mode, two things can happen. 
          If the file does not exist, a new file is created for reading as well as writing .If the file already exists and has some data stored in it, the contents are overwitten."""

""" a :- Opens a file for appending . The file pointer is placed at the end of the file if the file exists . If the file does not exist, it creates a new file for writing."""

""" ab :- Opens a file in binary format for appending . The file pointer is at the end of the file if the file exists. If the file does not exist , it creates a new file for writing ."""

""" a+ :- Opens a file for both reading and appending. The file pointer is placed at the end of the file if the file exists . If the does not exist, it creates a new file for reading and writing."""

""" ab+ :- Opens a file in binary format for both reading and appending. The file pointer is placed at the end of the file if the file exists . If the file does not exist , a new file is created for reading and writing. """


#The Object Attributes 
"""Using the file object, you can easily access different types of information related to that file. This information cna be obrained by 
reading values of specific attributes of the file"""

f1=open("file_handling.txt","r+")
print(f1)
f1.close

print("\nProgram topen a file and print its attribute values.\n")
file=open("File.txt","wb")
print("Name of the file: ",file.name)
print("File is Closed .", file.closed)
print("File has been opened in ", file.mode,"mode")


#The close() method as the name suggests in used to close the file object. 

#programming tip:- Python automatically closes a file when the reference object of a ifle is reassigned to another file, but as a good programming habit you should always explicitly use the close() method to close a file 
#syntax :- fileObj.close()

#There is an upper limit o the number of files a progra can open . if that limit is exceeded then the program may even crash or work in an unexpected manner. 

print("\nProgram to access a file after it is closed.\n")
file=open("File.txt","wb")
print("Name of the file: ", file.name)
print("File is closed .",file.closed)
print("File is now being closed.. You cannot use the File Object.")
file.close()
print("file is closed.",file.close)

#Note :- Python has a garbage collector to clean up unreferenced objects but still it is our responsibility to close the fiel and realese the resources consumed by it.

#read() and write are used to read data from file and write data to files respectively . 

#The write() method is used to write a string to an already opend file.

"""syntax:- fileObj.write(string)"""

print("\nProgram that writes a message in the file, File1.txt \n")

file = open("File.txt","r+")
file.write("Hello all, hope you are enjoying lealrning Python")
print(file.write("\n Hello all, hope you are enjoying lealrning Python"))
file.close()
print("Data Written into the file........")

#Note :- The write() method returns None

print("Program to write to a file using the writelines() ,method.")

file=open("File.txt","w")
lines=["Hello World,","Welcome to the world of Python ","Enjoy Learning Python"]
file.writelines(lines)
file.close()
print("Data written to file.....")

"""Note that if you open a fiel in 'w' or 'wb' mode an then start writing data into it, then its 
existing contents would be overwritten .So always open the file in 'a' or 'ab' mode to add more data to existing data stored in the file."""

print("\nProgram to append data to an already existing file.")
file = open("File.txt","a")
file.write("\n Python is a very simple yet powerful language.")
file.close()
print("Data appended to file .......")

#Note :- If you open a file in append mode then the file is created if it did not exist.

#The read() and readline() Methods 
#syntax:- fileObj.read([count])
"""count is an optional parameter which if passed to the read() method specifies the number of bytes to be read from the opened file."""

print("\n Program to print the first 10 characters of the 'File.txt' \n")

file=open("File.txt","r")
print(file.read(10))
file.close()

#Note that if you try to open a file for reading that does not exist , then you will get an error.

#Note:- read() method returns newlines as '\n'.

file=open("File.txt","a+")
lines=["\nHello All,","\n ","\nHope you are enjoying learning Python ","\nWe have tried tocover every point in deatail to avoid confusion","\nHappy Reading"]
file.writelines(lines)
file.close()


print("\n\n")
f1=open("File.txt","rb")
print(f1.read())
f1.close()

print()

#Programming Tips :- Binary files are more efficient than text files so we have opened the files using rb and wb access modes. You could have aslo opened using r or w access mode to work with text files.

#Note:- After reading a line from the file using the readline() method , the control automatically pases to the next line. That is why , when you call readline() again , the next line in the file is returned.

print("Program to demonstrate readlines() function.")
file=open("File.txt","r")
print(file.readlines())
print()
file.close()
print("File is closed now or not ",file.closed)

print()


#The list() method is also used to display entire contents of the file.you just need to pass the file object as an argument to the list() method.

print("\nProgram to display the contents of the file File.txt using the list() method.")
print()
file=open("File.txt","r")
print(list(file))
file.close()
print(file.closed)

print("\nProgram to display the contents of a file.")
print()
file = open("File.txt","r")
for line in file:
    print(line)
file.close()

"Note :- All reading methods return an empty string when end-of-file(EOF) is reached .That is , if you have to read the entire file and then again call readline(), an empty string would be returned."

#Opening Files using with Keyword

"""Advatages of with  is file is properly closed after is used even if an error occurs during read or write operation or even 
when you forget to explicitly close the file. This difference is clearly evident from the code given as follows using the contensts
of file.txt ."""

print("\nProgram 1 \n")
with open("File.txt","rb") as file:
    for line in file:
        print(line)
print("Let's check if the file is closed : ", file.closed)


print("\nProgram 2\n")
file = open("File.txt","rb")
for line in file:
    print(line)
print("Let's check if hte file is closed:  ",file.closed)

file.close()
print(file.closed)

"""Note :- Calling close() on a file object that is already closed does not raise any error but
fails silently as shown below.""" 

print("\nProgram 3\n")
with open("File.txt","r") as file:   #file is already closed after the last line is read
    print(file.read())      #attempt to close a file that is already closed 
print(file.closed)
file.close()

"""Note :- When you open a file for reading or writing , the file is searched in the current working directory.
If the file exists somewhere else then you need to specify the path of hte file."""

#Splitting words 

"""Python allows you to read line(s) from a file and splits the line (treated as a string) based on a character .By default,
this character is space but you can even specify any other character to split words in the string."""

print("\nProgram to split the line into a series of words and use space to perform the split operation.\n")
with open("File.txt","r") as file:
    line=file.readline()
    words = line.split()
    print(words)

with open("File.txt","r") as file:
    line = file.read()
    print(line)
    print(line.split(","))
    print(file.closed)
    file.close()
    print(file.closed)
    print()

with open("File.txt","r") as file:
    print(file.read())
    print(file.closed)
    print(file.read().split())
    print(file.closed)

#Program to perform split operation whenever a comma is encountered.
print()
with open("File.txt","r") as file:
    line = file.readline()
    words = line.split(',')
    print(words)
    print(file.closed)
    file.close()
    print(file.closed)

#Some Other Useful File Methods

" fileno() :- Returns the file number of the file (which is an integer descriptor) "

file = open("File.txt","r")
print(file.fileno())
file.close()
print()

" flush() :- Flushes the write buffer of the file stream "
file = open("File.txt ","w")
file.write("Hello")
print(file.isatty())
file.close()
print()

" readline(n) :- Reads and returns one line form file. n is optionsl . if n is spcified then atmost.n bytes ae read."
file = open("File.txt","r")
print(file.readline(10))
file.close()
print()

"truncate(n) :- Resizes the file to n bytes"
file = open("File.txt","a+")
file.write("Welcome to the world of programming..")
file.truncate(5)
file = open("File.txt","r")
print(file.read())
file.close()
print()

"rstrip() :- Strips off whitespace including newline characters from the right side of the string read from the file"
file = open("File.txt")
line = file.readline()
print(line.rstrip())
file.close()
print()


#File Positions
"With every file , the file managment system associates a pointer often known as file pointer that faciliates the movement across the file for reading and/ or writing data."
"""The file pointer specifies a location from where the current read or write operation is initiated.

Python has various methods that tells or sets the position of the file pointer. For example, the tell() method
tells the current positon within the file at which the next read or write opration will occur. It is specified as number of bytes form the beginning of the file.

When you just open a file for reading , the file pointer is positioned at location 0, which the beginning of the file."""

#syntax :- seek(offset[,from])
"""The seeIoffset[,form ] method is used to set the postion of hte file pointer of hte file pinter or in simple terms ,
move the file pointer to a new location. The "offset" argument indicates the number of bytes to be moved and the from argument specifies the reference position from
where the bytes are to be moved. """

print("\nProgram that tells and sets the position of the file pointer.\n")
file = open("File.txt","rb")
print("Position of file pointer before reading is : ",file.tell())
print(file.read(10))
print("Position of file pointer after reading is : ",file.tell())
print("Setting 3 bytes from the current position of file pointer")
file.seek(3,1)
print(file.read())
file.close()

"Note :- In Python , you don't need to import any library to read an write files.just create a file object and call the open function to read/write to the file."


with open("File.txt","r+") as file:
    print("Position of file pointer before reading is : ",file.tell()  )
    print(file.read(10))
    print("Position of file pointer after reading is : ",file.tell())
    print("Setting 3 bytes froom the current position of file pointer ")
    file.seek(3,0)
    print(file.read())
    file.close()

#Program to add some text to the experimental File name as "File.txt"
file=open("File.txt","a+")
line=["Hello","\nmy name is rema theraja ","\nI am here to teach you python ","\nEnjoy the python learning"]
file.writelines(line)
file.write("\nLets learn python")
print(file.read())
file.close()

#Program to see the changes of the position of the pointer in the experimental file name as "File.txt when we opne with different mode ."
file=open("File.txt","a+")
print(file.tell())
file.close()

file=open("File.txt","r")
print(file.tell())
file.seek(95,file.tell())
print("Position of the pointer now in the file :",file.tell())
print(file.read())
file.close()

#Program to see the negative indexing in the readline() command .
file = open("File.txt","a+")
file.readline(-2)
file.close()

#rough work in file handling
file = open("File.txt","a+")
print(file.fileno())

file.close()


"don't comment out this code another the code written in the file is flush "
# file=open("File.txt","w")
# file.flush()


print()
"don't comment out this code another the sentences written in the file is overwritten"
# file = open("File.txt","w")
# file.write("Hello")
# print(file.isatty())
# file.close()

#truncate(n)

"don't comment out this code another the sentences writen in the  file is overwritten"
# file=open("File.txt","a+")
# file.write("\nWelcome to the world of programming...")
# file.truncate(10)
# print()
# file=open("File.txt","r")
# print(file.read())


file = open("file.txt","r")
line=file.readline()
print(line.rstrip())

#Programming Exmaples
"Write a program that copies first 10 bytes of a binary file in to another."
with open("File.txt","rb") as file:
    with open("File2.txt","wb") as file2:
        buf = file.read()
        file2.write(buf)
print(file.closed,file2.closed)
file.close()
print("File Copied")

"Write a Program that copies one Python script into another in such a way that all comment lines are skipped and not copied in teh destination  file ."
with open("First.py","rb") as file1:
    with open("Second.py","wb") as file2:
        while 1:
            buf =file1.readline()
            if len(buf) !=0:
                if buf[0] == "#":
                    continue 
                else:
                    file2.write(buf)
            else:
                break
print(file1.closed,file2.closed)
print("File Copied")

file1=open("First.py","rb")
print(file1.read())
file1.close()

"Write a program that accepts filename as an input form the user .Open the file and count the number of times a character apperars in the file."
filename="File.txt"
with open(filename,"r") as file:
    buf = file.read()
    character ="b"
    num=0
    for char in buf:
        if char == character:
            num+=1
print(file.closed)
print(num)
print("The number of the %c character in the %s is %d"%(character,filename,num  ))

file = open("file.txt","r+")
print(file)

"Write a program that reads data from a file and calculates the percentage of vowels and consonants in the file."
with open("File.txt") as file:
    text=file.read()
    vowels_count=0
    consonants_count=0
    for char in text:
        if char in "aeiouAEIOU":
            vowels_count+=1
        else:
            consonants_count+=1
print("Numbers  of the Consonants is %d in the %s."%(consonants_count,"File.txt"))
print("Numbers  of the vowels is %d in the %s."%(vowels_count,"File.txt"))
print("Percantage of the Vowels is %d  "%(((vowels_count/len(text))*100)))
print("Percentage of the consonants is %d  "%((consonants_count/len(text)*100)))

#RENAMING AND DELETING FILES
"""The os module in Python has various methods that can be used to perform file-processing operations like renaming 
and deleting files.To use the methods defined in the os module, you should first import it in your program and then call any related functions."""

"The rename() Method :- The rename() method takes two arguments ,t he current filename and the new filename ."
#syntax :- os.rename(old_file_name,new_file_name)
#Programming Tip :- The file object provides functions to manipulate files.

print()
"Program to rename file 'File.txt' to 'file_handling2.txt"

"Don't run the below program because the file name is updated ."
# import os 
# os.rename("File.txt","File_handling2.txt")
# print("File Renamed")

"The remove() Method: This method can be used to delete file(s).The method takes a filename(name of the file to deleted ) as an argument an deletes that file."
#Syntax :- os.remove(file_name)

"I can't perform the above program because I don't want to delete any file from my directory."

#Directory Methods
"The mkdir() Method :- The mkdir() method of the os module is used to create directories in the current directory."
#syntax :- os.mkdir("new_dir_name"

"Program to create a new directory in the current directory."
# import os 
# os.mkdir("New Dir")
# print("diretory is created.")

"Don't execute the above repetadly it will create the new directory ."

"The getcwd() Method:- The getcwd() method is used to display the current working directory (cwd) ."

#Programming Tip:- You must use escape sequence when using the backward slash.
#The syntax of getcwd() is :- os.getcwd()

"The chdir() Method :- The chdir() method is used to change the current directory .The method takes the name of the directory which you want to make the current directory as an argument."
#Syntax :- os.chdir("dir_name")


"Program that current directory to our newly created directory - New Dir"
# import os
# print("Current working Directory is : ", os.getcwd())
# print("After the changes the path of the current working directory ...",end=" ")
# os.chdir("New dir")
# print("Current working direcotory is ",os.getcwd())

"Don't execute the above program because it change teh directory ."

"""The rmdir() Method :- The rmdir() method is used to remove or delete a directory .For this , it accepts 
the name  of the directory to be deleted as an argument .However ,before removing a directory, it should be absoultely empty and all the contents in it should be removed."""
#The syntax of remove() method is :- os.rmdir("dir_name")


"Program to demonstrate the use of rmdir() function."
# import os 
# os.chdir("D:\python programming study material (link , websites name, docs...)")
# # os.rmdir("New Dir")
# print("Directory Deleted ....")

"Again  Don't execute the above progam it will remove the New Dir experimental directory."

#Programming Tip:- To remove a non-empty directory , use the rmtree() method defiend inside the shutil.module.

"""If you try to delete a non-empty directory, then you will get OSError: [WinError 145] The directory is not empty.If you still 
want to delete the non-empty directory,use the rmtree() method defined in the shutil module as shown below"""

# import shutil
# shutil.rmtree("New Dir")

"The makedirs() Methods :- The method makedirs() is used to create more than one folder .for example, if you pass string C:Python34\Dir1\Dir2\Dir3 as an argument to makedirs() method, then Python wil create folder Dir1 i Python34 folder,Dir2 in Dir1 folder , and Dir2 folder in Dir1 folder, and dir3 in the Dir2 folder ."
# import os 
# os.makedirs("D:\python programming study material (link , websites name, docs...)\\Dir1\\Dir2\\Dir3")

#Note:- we have put \\ slashes in the string so that the first slash acts as an escape 

"Don't Comment out the above program."

#Programming Tip :- If you use a method defined in a module without importing that module , then you will get a NameError.
"Program that uses os.path.join() method to form a valid file path "
# import os 
# print(os.path.join("c:","students","under graduate ","BTech.docx"))


"Program to print the absoulte path of a file using os.path.join"
# import os
# path="d:\\="
# filename = "First.txt"
# abs_path=os.path.join(path,filename)
# print("ABSOLUTE FILE PATH = ",abs_path)
# file = open(abs_path,"wb")
# file.write("Hello")
# file.close()
# file=open(abs_path,"r")
# print(file.read())

#Methods from the os Module
"""The os.path.abspath() Method : This method uses the string value passed to it to form an absoulte path.
Thus , it is another way to convert a relative path to an absolute path."""

#Program to demonstrate the use of os.path.abspath() method

# import os
# print(os.path.abspath("Python\\Strings.docx"))
# print(os.getcwd())

"""The os.path.isabs(path) Method : This method accepts a file path as an argument and returns True if 
the path is an absolute path and False otherwise."""

#Program to demonstrate the use of os.path.isabs() method

import os
print("os.path.isabs(\"Python\\Strings.docx\")= ",os.path.isabs("Python\\Strings.docx"))
print("os.paht.isabs(\"C:\\Python34\\Python\\Python\\Strings.docx\") = ",
os.path.isabs("C:\Python34\Python\\Strings.docx"))


"""The os.path.relpath(path,start) Method:- This method accepts a file path and a start string
as an argument and returns a relative path that begins form the stat.IF start is not given ,the current directory is taken as start."""
#Program to demonstrate the use of os.path.relpath() method
import os
print("os.path.relpath(\C:\\Python\\Chapters\\FirstDraft\\Stright.docx\")= ",
os.path.relpath("C:\Python\Chapters\FirstDraft\Strings.docx","C:\Python"))

"""The os.path.dirname(path) Method :- This method returns a string that includes everything specified in the path 
(passed as argument to the method ) that comes before the last slash."""

"""The os.path.basename(path) Method :- This method returns a string that includes 
everything specified in the path (passed as argument to the method ) that comes after the last slash."""

#Programming Tip:- Do not combine paths using string concatenation (+).Rather , use os.path.join() method .
# import os
print("os.path.dirname(\"C:\\Python\\Chapters\\First Draft\\Strings.docx\") = ",
os.path.dirname("C:\Python\Chapters\First Draft \ Strings.docx"))

print("\n os.path.basename(\"C:\\Python\\Chapters\\First Draft\\Strings.docx\") = ",
os.path.basename("C:\Python\Chapters\First Draft\Strings.docx"))

"The os.path.split(path) Method : This method accepts a file path and returns its directory name as well as the basename. So it is equivalent to using two separate methods os.path.dirname() and os.path.basename()"

print("Program to demonstrate the use of os.path.split() method ")

# import os
print("os.path.split(\"C:\\Python\\Chapters\\First Draft\\Strings.docx\") = "
,os.path.split("C:\Python\Chapters\First Draft\Strings.docx"))

"The os.path.getsize(path) Method : This method returns the size fo the file specified in the path arguments."

"The os.listdir(path) Method : This method returns a list of filenames in the specified path."

print("Program to demonstrate the use of os.path.getsize() and os.listdir() methods.")
# import os
# print("os.path.getsize(\"C:\\Python34\\Try.py\") = ",
# os.path.getsize("C:\\Python34\\Try.py"))

# print("\nos.listdir(\"C:\\Python34\") = ",os.listdir("C:\Python34"))

"The os.path.exists(path) Method: The method as the name suggests accepts a path as an arguments and returns True if the file or folder specified in the path exists and False otherwise."

"The os.path.isfile(path) Method: The method as the name suggests accepts a path as an argument and returns True if the path specifies a file and False otherwise."

"The os.path.isdir(path) Method : The method as the name suggests accepts a path as an argument and returns True if the path specifies a an existing directory and False otherwise."

# import os
print("os.path.exists(\"C:\\Python34\\Dir1\") = ",
os.path.exists("C:\Python34\Dir1"))

print("os.paht.isfile(\"C:\\Python34\\Dir1\") = ",
os.path.isfile("C:\Python\Dir1"))

print("os.path.isdir(\"C:\\Python34\\Dir1\") = ",
os.path.isdir("C:\Python34\Dir1"))

print("os.path.isfile(\"C:\\Python34\\Try.py\") = ",
os.path.isfile("C:\Python34\Try.py"))

print("os.path.isdir(\"C:\\Python34\\Try.py\") = ",
os.path.isdir("C:\Python34\Try.py"))

print("Write a program that counts the number of tabs , spaces, and newline characters in  a file.")
filname="File.txt"
with open(filename) as file:
    text=file.read()
    count_tab=0
    count_spaces=0
    count_newline=0
    for word in text:
        if word=="\n":
            count_newline+=1
        if word=="\t":
            count_tab+=1
        if word==" ":
            count_spaces+=1
file.close()
print("The number tabs occur in the file is ",count_tab)
print("The number of the spaces in the file is ",count_spaces)
print("The number of the newline in the file is ",count_newline)

print("Write a  program that coumputes the total size of all the file sin C:\Python34 folder.")
import os
total_Size=0
for file in os.listdir("D:\Programming language\python programming and other progrmming language"):
    total_Size+=os.path.getsize(os.path.join("D:\Programming language\python programming and other progrmming language",file))
print("Total size of all the files in D:\Programming language\python programming and other progrmming language = ",total_Size)


print("\nWrite a program to check if flash drive is connected to your coumputer .")
# import os 
print("os.path.exists(\"G:\ \")=",os.path.exists("G:\\"))

print("Write a program that reads a file line by line . Each line read from the file is copied to another file with line numbers specified at the beginning of the line.")
file1=open("File.txt")
file2=open("File1234.txt","w")
num=1
for line in file1:
    file2.write(str(num) + " : " + line)
    num+=1
file1.close()
file2.close()


print("\nWrite a program that generates a Quiz and uses two files - Questions.txt and Answers.txt. The program opens Question.txt and reads a question and displays the question with options on the screen . The program then opens the Answer.txt file and displays the correct answers.\n")
file1=open("Questions.txt","r")
file2=open("Answer.txt","r")
ques=file1.read()
qlines=ques.split('\n')
for lines in qlines:
    print(lines)
ans=file2.read()
alines=ans.split('\n')
print("CORRECT ANSWERS")
for lines in alines:
    print(lines)


print("\nWrite a program that fetches data from a specified url and prints it on screen.")
import urllib.request
x=urllib.request.urlopen("https://google.com/")
google=str(x.read())
file=open("File.txt","a+")
file.write(google)

print("\nWrite a program that fetches data from a specified url and writes it in a file .\n")
#Hint:- Use the urllib2 module that handles the url

url="https://www.google.com/serch?q=python"
headers={}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML,like Gecko ) Chrome/24.0.1312.27 Safari/537.17"
Request=urllib.request.Request(url,headers=headers)
Response=urllib.request.urlopen(Request)
Data=Response.read()
File=open("URL_File.txt","w+")
File.write(str(Data))
File.close()
print("Contents Written in the file.......")