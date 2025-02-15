#program to calculate the factorial of a number recursively.

#the recursive program contain the two important part of the function :-1)bash program 2)recursive program
#1)bash program is essential to stop the continous execution of the recrusive program
#2)recursive program is used to repeat the program as a loop in the main funtion

def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
print("The factorial of the number is ",fact(5))

#program to calculate exp(x,y) using recursive functions.
def exp(n,y):
    if y==0:
        return 1
    else:
        return n*exp(n,y-1)
n=5
m=3
print("Resul=",exp(n,m))

#program to print teh Fibonacci series using recursion.
def fibo(x):
    if x<2:
        return 1
    return fibo(x-1)+fibo(x-2)
x=input("Enter the number os terms:-")
for i in range(x):
    print("The fibonacci series is the ",fibo(i))

#The above funtion gives you error so resolbe it and we will be continued to above topic ..... se you soon.