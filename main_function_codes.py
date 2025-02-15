#program using functions to check whether two numbers are equal or not.
def check_relation(a,b):
    """Program display the greater number 
    between two number given as a parameters in arguments. """
    if a<b:
        return 1
    elif b<a:
        return -1
    else:
        return 0
a=3
b=5
r=check_relation(a,b)
if r==1:
    print(str(b)+" is the greater numaber than "+str(a)+".")
elif r==-1:
    print(str(a)+" is the greater number than "+str(b)+".")
else:
    print(str(a)+" and",str(b),"is the equal numbers.")

#program to swap two numbers.
def swap(a,b):
    """program to swap the two numbers.
    """
    a,b=b,a
    print("After swap>>","\na=",a,"\nb=",b)
a=int(input("Enter the number \n>>>"))
b=int(input("Enter the number \n>>>"))
print("Befor swap>>>","\na=",a,"\nb=",b)
print(swap(a,b))

#program to return the full name of a person.
def name(full_name,last_name):
    """program to generate the full name of  the person.

    Args:
        full_name (string): Its a name ofthe person.
        last_name (string): Its a surname of the person
    """
    separator=" "
    n=full_name+separator+last_name
    return n
print(name("Janak","Raj"))

#program to return the average of its arguments.
def aveg(num1,num2):
    """Program while give the average of the given arguments

    Args:
        num1 (num): Its a numbers
        num2 (num): Its a number
    """
    sum2=num1+num2
    a=sum2/2
    return a
print("Average ="+str(aveg(5,7)))

