#program to demonstrate the lambda function.
sum=lambda x,y:x+y
print("Sum = ",sum(7,5))

#program to demonstrate the lambda function to find smaller between two functions.
def small(a,b):
    if(a<b):
        return a
    else:
        return b
sum1=lambda x,y:x+y
differ=lambda x,y:y-x
print("Smaller number is ",small(sum(-3,-2),differ(-1,2)))

#program to use a lambda function with an ordinary function.
def increament(y):
    return (lambda x: x+1)(y)
a=100
b=increament(a)
print("The value of the a "+str(a),"\nThe value of the a after increament is "+str(b))

#programt to demonstrate the use of the lambda function assigned to the variable twice.
twice=(lambda x:x*2)
print(twice(9))

#program to demostrate the use of the lambda function without assigned to  any variable.
print((lambda x:x*2)(9))

#program to demonstrate taht passes lambda functions as an argument to a function.
def func(f,n):
    print(f(n))

twice=lambda x:x*2
thrice=lambda y:y*3
func(twice,4)
func(thrice,3)

#program to add two numbers using lambda function.
add =lambda x,y:x+y #lambda function that adds two numbers 
#lambda function that calls another lambda function to geneate the result
multiply_and_add=lambda x,y,z:x*add(y,z)

print(multiply_and_add(3,4,5))

#program to show a multi-line doocstring 
def func():
    str = "Hello world"
    """The progam just prints a message.
    It well display Hello World !!!
    """
    print("Hello World")
func()
print(func.__doc__)
