#below program is the experiment on the pattern printing for loop .
print("Write the program to print the below pattern .")
for j in range(1,6):
    for i in range(j,0,-1):
        print(i,end=" ")
    print()

print("Program to print the below pattern.")
for i in range(1,5):
    print("PASS ",i,"=",end=" ")
    for j in range(6):
        print(j,end=" ")
    print()

print("Program to demostrate the spaces using for loop ")
for x in range(5,0,-1):
    print(" ",end=" ")
print("k")
                            #imp:- both will give the same output but preferred the reversed order because it was efficiently used in for loop .


print("The Program was finised.")
for x in range(1,6):
    print(" ",end=" ")
print("k")

print("Program was finised.")
for x in range(1,11):
    print(x,end=" ")
for j in range(10,0,-1):
    print(j,end=" ")

for x in range(1,6):
    print()
    for j in range(1,x+1):
        print(x,end=" ")
print("Program was finised.")


N=5
for a in range(1,N+1):
    for j in range(N,a,-1):
        print(" ",end=" ")
    for x in range(1,a+1):
        print(a,end=" ")
    for p in range(a-1,0,-1):
        print(p,end=" ")
    print()
print("Program was finised .")

N=5
for a in range(1,N+1):
    for j in range(N,a,-1):
        print(" ",end=" ")
    for x in range(1,a+1):
        print(a,end=" ")
    print()

import string
count=ord("A")
for x in range(1,26):
    print(chr(count),end=" ")
    count+=1
    for j in string.ascii_lowercase[x-1]:
       print(j,end="")
    print()
    print(end=x*" ")

pattern=r"[a-zA-Z]+ \d+"
print(pattern)



for x in range(0,26):
    ch="A"
    print()
    for j in range(1,x+1):
        print(ch,end=" ")
        ch=chr(ord(ch)+ 1) 



#Program to demosntrate the printing the string by using the string module.
import string
print(string.ascii_uppercase)
for x , j in zip(string.ascii_uppercase,string.ascii_lowercase):
    print(f"{x}={ord(x)} and {j}={ord(j)}")

#both program give the same output but bothe have the different methods

for i in range(len(string.ascii_uppercase)):
    x=string.ascii_uppercase[i]
    j=string.ascii_lowercase[i]
    print(f"{x}={ord(x)} and {j}={ord(j)}")

#When you pass a string value of file and folder names that makes up the path , then os.path.join() method will return a string with a file path that has correct path separtors.
import os 
print("The path is :- ",os.path.join("\bc:","students","under graduate","BTech.docx"))


print("This is your program .")
#Program to print the absoulte path of a file using os.path.join 
# import os 
# path = "d:\\="
# filename = "First.txt"
# abs_path=os.path.join(path,filename)
# print("ABSOULTE FILE PATH = ","w")
# file = open(abs_path,"w")
# file.write("Hello")
# file.close()
# file=open(abs_path,"r")
# print(file.read())


#method form teh os module 
print("Program to deomonstrate the use of os.path.abspath() method.")
import os
print(os.path.abspath("Python\\Strings.docx")) 

print("This is our next program.\n")
print("os.path.isabs(\"Python\\Strings.docx\") = ",
os.path.isabs("Python\\Strings.docx"))
print("os.path.isabs(\"C:\\Python34\\Python\\Strings.docx\" ) = ",
os.path.isabs("C:\Python34\Python\Python\\Strings.docx"))

print("\nThis is our new program .")
print("os.path.relpath(\"C:\\Python\\Chapters\\First Draft\\Strings.docx\" ) = ",
os.path.relpath("C:\Python\Chapters\First Draft\Strings.docx ","C:\Python"))

import string

list1=[x for x in range(1,11)]
list2=[x for x in string.ascii_letters]
list3=list1+list2
print(list1,list2,list3)
print(id(list1),id(list2),id(list3))

# Toppers=(("Arav","Bsc",92.0),("Chaitanya","BCA",99.0),("Dhruvika","Btech",97))
# for i in Toppers:
#     print(i)
# choice=input("Do you want to edit the details : ")
# if choice=='y':
#     name=input("Enter the correct name: ")
#     new_course=input("Enter the correct course : ")
#     new_aggr=input("Enter the correct aggregate :- ")
#     i=0
#     new_Toppers=()
#     while i<len(Toppers):
#         if Toppers[i][0] == name:
#             new_Toppers+=(name,new_course,new_aggr)
#         else:
#             new_Toppers+=Toppers[i]
#         i+=1
# for i in new_Toppers:
#     print(i,end=" ")

print("\nWrite a program to subract the matrix A from matrix B .\n")
A=[[1,2,3],
   [5,6,7]]
B=[[3,9,8],
   [9,5,5]]
R=[[0,0,0],
   [0,0,0]]
for x in range(len(A)):
    for j in range(len(A[x])):
        R[x][j]=B[x][j]-A[x][j]
print(R)

print(float(-1))


print("hello")
import string

def missingCharacters(s):
    # Write your code here
    num=""
    low=""
    num2=""
    low2=""
    for word in s:
        if word.isnumeric:
            num+=word
        if word.isalpha() and word.islower():
            low+=word

    for word2 in string.ascii_lowercase:
        if word2 not in low:
            low2+=word2
    for n in range(10):
        if str(n) not in num:
            num2+=str(n)
    sorted1=sorted(num2)
    sorted2=sorted(low2)

    string23=''.join(sorted1+sorted2)

    return string23
print(missingCharacters(s='7985interdisciplinary12'))


# print('The List comprehension hackerrank')
# n1=1
# n2=1
# n3=2
# n45=3

# list_array1=[ [x,y,z]   for x in range(n1+1)  for y in range(n2+1) for z in range(n3+1) ]
# def check12(lis):
#     if sum(lis)<n45:
#         return lis
# list_arra1=list(filter(check12,list_array1))
# print(list_arra1)



# n = int(input())
# arr = list(map(int, input().split()))
# arr.remove(max(arr))
# print(arr)