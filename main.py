#calculator
a=45 #variable=value
b=56
print(b/a) #divident oprator
print(a+b) #addition oprator
print(a-b) #substract oprator
print(a*b) #multiply oprator

#program to find a flat rs 500,if purches amount is grater than 2000
a=int(input("Enter a amount you purches= "))
if a>2000:
    A=a-500
    print('You are amount is',A)
else:
    print("You are amount is",a)
    


#provide a extra marks,if player belongs to sporst catagory
marks=int(input("Enter your marks=  "))
catagory=input("Enter your catagory:-  ")
if catagory=="sport":
    print(marks+5)
elif(catagory=="genral"):
    print(marks)
else:
    print("invalid spelling,Check your spelling.")