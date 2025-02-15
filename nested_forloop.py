#write a program to print the following pattern .
for x in range(1,6):
    print("PASS =",x)
    for j in range(1,5):
        print(j,end=" ")
    print()

for x in range(1,6):
    print("PASS =",x,end=" ")
    for j in range(1,4):
        print(j, end=" ")
    print()

#The above pattern are you find in the book of " Python programming using problem solving approach"

for x in range(1,6):
    print()
    for j in range(4):
        print("*",end="")
print("\ntask was finish")
    

for j in range(6):
    print("")
    for i in range(j):
        print("*",end="")

for k in range(1,6):
    print()
    for x in range(1,k+1):
        print(x,end=" ")
print("\n TASK HAS BE EXECUTED ")

for o in range(1,6):
    print()
    for i in range(1,1+o):
        print(o,end=" ")

print("\n\nWrite a program to print the following pattern.")
count = 0
for i in range(1,5):
    print()     #prints  a new line
    for j in range(1,i+1):
        print(count,end=" ")
        count+=1


#IMPORTANT PROGRAM:- This program is essential for understand the reverse printing of the n number by using for loop.
print("Program to print the number in the reverse order by using the for loop .")
for i in range(6,0,-1):
    print(i,end=" ")

print("\n\nWrite a program to print the following pattern.")
N=5
for i in range(1,N+1):
    for k in range(N,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print("Write a program to print the following pattern.")
N=5
for i in range(1,N+1):
    for k in range(N,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for l in range(i-1,0,-1):
        print(l,end=" ")
    print(" ")

print("Program was finised .")

N=5
for i in range(1,N+1):
    for k in range(N,i,-1):
        print("",end=" ")
    for j in range(1,i+1):
        print(i,end=" ")
    print()