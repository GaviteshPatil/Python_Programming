def program34():
    #program to display the average of the first n nature numbers.
    s=0
    for x in range(0,11):
        s +=x
    print("The sum of the first '10' natural numbers is "+str(s))

def program35():
    #program to print the average of the first 10 n numbers.
    num=int(input("Enter the numbers:- \n>>>"))
    average=0
    st=0
    for x in range(1,num+1,):
        st +=x
    average=st/num
    print("The sum of the numbers is "+str(st))
    print("The avrage of the numbers is "+str(average))

def program36():
    #program to display the multiplication tables.
    num1=int(input("Enter the numbers:- \n>>>"))
    print("The multiplication table of "+str(num1)+" number .")
    for x in range(1,11):
        print(str(num1)+"x"+str(x)+"="+str(num1*x))

def program37():
    #program to display the even or odd numbers in the list.
    num3=int(input("Enter the numbers :- \n>>>"))
    print("The following numbes is the even or odd ")
    for x in range(1,num3+1):
        if x%2==0:
            print(x,"is the even numbers.")
        else:
            print(x,"is the odd   numbers.")
def program38():
    #program to display the factorial of the n numbers.
    factorial=1
    num4=int(input("Enter the numbers:- \n>>>"))
    for p in range(1,num4+1):
        factorial *=p
    print("The factoral of the "+str(num4)+" is "+str(factorial))

#program to check wheather the number is prime number or composite.
def program39():
    num=int(input("Enter the nuber \n>>>"))
    q=0
    for x in range(2,num):
        if num%x==0:
            q=1
            break
    if q==1:
        print("Its a compositional number.")
    else:
        print("Its a prime number.")

#program using the while loop to read the numbers until -1 is encoluntered.Also count the number of prime numbers and composition numbers entered bythe users.

def program40():
    num1=1
    num2=0
    num3=0
    while 1:
        num=int(input("Enter the number\n>>>"))
        if num==-1:
            break
        for x in range(2,num):
            if num%x==0:
                num1=0
            else:
                num1=2
        if num1==0:
            num2+=1
        else:
            num3+=1
    print("Total prime number is "+str(num3))
    print("Total composition numberm "+str(num2))

#program to calculate pow(x,n).
def program41():
    num=int(input("Enter the number \n>>> "))
    num2=int(input("Enter till the power  "))
    answer=1
    for x in range(1,num2+1):
        answer =answer*num
    print("The"+str(num)+" till the power "+str(num2)+"is "+str(answer))

#program to calculate all leap years from 1900-2101.
def program42():                                        #we need to modify this code .
    print("The leap years from 1900-2101 are :")
    for x in range(1900,2102):
        if x%4==0:
            print(x,end=" ")

#program to sum the series--1/1
def program43():
    n=int(input("Enter the number\n>>>"))
    sum1=1/1
    for x in range(2,n+1):
        sum1+=(1/(x**2))
    print("The sum of the is "+str(sum1))

#program to sum the series--1/1+1/2..1/n.
def program44():
    n=int(input("Enter the number \t:-"))
    sum1=0
    for x in range(1,n+1):
        sum1+=1/x
        print("1/"+str(x),end=' ')
    print("\nThe sum of the series is "+str(sum1))

#program to sum the series--1/2+2/3+...+n/(n+1).
def program45():
    n=int(input("Enter the number \n>>>"))
    x=0
    sum1=0
    for p in range(1,n+1):
        sum1+=p/(p+1)
        x=p+1
        print(str(p)+"/"+str(x),end=" | ")
    print("\nThe sum of the series is "+str(sum1))

#program to sum the series--1/1+2
def program46():
    n=int(input("Enter the number\n>>>"))
    sum1=0
    p=0
    for x in range(1,n+1):
        sum1+=(x**x)/x
    print("The sum of the series is "+str(sum1))

#program to calculate sum of cubes of numbers from 1-n.
def program47():
    n=int(input("Enter the numbers \n>>>"))
    sum1=0
    for x in range(1,n+1):
        sum1+=x**3
    print("The sum of the cubes of 1-n numbers is "+str(sum1))

#program to calculate the sum of squares of even numbers.
def program48():
    n=int(input("Enter the numbers \n>>>"))
    sum1=0
    for x in range(1,n+1):
        if x%2==0:
            sum1+=x**2
    print("The sum of the squres of the even numbers is "+str(sum1))

def program49():
    n=int(input("Enter the start_day \t:-"))
    n1=int(input("Enter the total numbers of days in the month \t :-"))
    print("_________________________________________________________")
    print("Sunday Monday Tuesday Wednesday Thursday Friday Saturday ")
    s=n1-1
    for x in range(s):
        print(end = "     ")

for x in range(1,6,5):
    print(" ")

def program50():
    num1=int(input("Enter the start day of month (1-7)\t:"))
    num2=int(input("Enter the number of days\t:"))
    print("Sun Mon Tues Wed Thurs Fri Sat")
    print("------------------------------")
    for x in range(num1-1):
        print(end="     ")
    i=num1-1
    for j in range(1,num2+1):
        if i>6:
            print()
            i=1
        else:
            i+=1
            print(str(j)+"      ",end="    ")

#Write a program to enter a decimal number. Calculate and display the binary equivalent of this number.
