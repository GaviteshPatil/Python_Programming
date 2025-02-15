for i in range(1,6):
    print("PASS",i,"-",end=" ")
    for j in range(1,6):
        print(j,end=" ")
    print()

#program to print the pattern.
for j in range(1,6):
    print("*",end=" ")
    for i in range(1,7):
        print("*",end=" ") 
    print()

for i in range(1,7):
    print()
    for j in range(1,i+1):
        print(j,end=" ")


for i in range(1,6):
    for j in range(1,7):
        print("*",end=" ")
    print()

for i in  range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

count=0
for i in range(1,5):
    print()  #print a new line
    for j in range(1,i+1):
        print(count,end=" ")
        count=count+1

#program to demonstrate the break statment.
for x in range(1,10):
    print()
count=0
while count<10:
    if count==5:
        print("\nDone")
        break
    else:
        count+=1
        print(count,end=" ")

#program to demonstrate the continue statment.
for x in range(10):
    if x==5:
        continue
    else:print(x,end=" ")
print("\nDone")


#program to demonstrate the square roots of a number.Demonstrate the use of break and continue statements.
import math
prime=0
composite=0

while 1:
    num=float(input("Enter the number:-\n>>>>"))
    if num==999 :
        print("Thanks for your , valuable time.")
        break
    elif num<0:
        continue
        print("The square root of the negative number is not calculated.")
    else:
        print("The squate root of the ",num,"is",math.sqrt(num))

#program that prompts users to enter numbers.The process will reapeat until user enters -1.Finally,the program prints the count of prime compostie numbers entered.
while 1:
    num=int(input("Enter the numbers:- \n>>>:"))
    if num==-1:
        print("Thankyou  for your valuable time .")
        break
    elif num>0:
        for x in range(1,num):
            if num%x==0:
                i=0
            else:
                i=1
        if i==0:
            print(num,"is composite number.")
        else:
            print(num,"is prime number.")
    else:
        print("The negative numbers is not allowed.")

#Using a for loop,write a program that prints out the decimal equivalent of 1/2,1/3,1/4....,1/10.
for i in range(1,10):
    print("1/",i,"=",1/i)


