import random as Rand

print("Its all the part of the exercise of the first chapeter.")
print("Write a program to enter two integers and then perform all arithmetic operations on them.")
int1=2
int2=4
print("\nThe addition operation is \n",int1+int2,end=" ")
print("\nThe substraction operation is \n",int2-int1,end=" ")
print("\nThe multiplication operation is \n",int1*int2,end=" ")
print("\nThe division operation is \n",int2/int1,end=" ")
print("\nThe modulo operstion to find the reminder of the division is \n",int2%int1,end=" ")
print("\nThe exponentional operation was used to find the exponention of the numbers is \n",int1**int2,end=" ")
print("\nTo find the quotient of the division \n",int2//int1,end=" ")

print("\n\n\nRepeat the program in Question 1 using floating point numbers.")
int1=4
int2=9
print("\nThe addition operation is \n",int1+int2,end=' ')
print("\nThe substraction operation is \n",int2-int1,end=" ")
print("\nThe multiplication operation is \n",int1*int2,end=" ")
print("\nThe division operation is \n",int2/int1,end=" ")
print("\nThe modulo operstion to find the reminder of the division is \n",int2%int1,end=" ")
print("\nThe exponentional operation was used to find the exponention of the numbers is \n",int1**int2,end=" ")
print("\nTo find the quotient of the division \n",int2//int1,end=" ")

print("\n\nWrite a program to perform string concatenation.")
str1,str2="Gavitesh","Patil"
print("\nThe concatenation of the strings is ",str1+str2)

print("\n\nWrite a program to demostrate printing a string within single quotes ,double quotes ,and triple quotes.")
print(""" \n The string in the 
      triple quotes .""")
print("\n\nThe string in the double quotes.")
print('The string in the single quotes')
print("The sting ' in the doublel quotes.")

print("\n\n Write a program to print the ASCII value of a character.")
count="A"
for j in range(0,26):
    print("The ASCII number of the ",count,"is",ord(count),end=" ")
    print()
    count=chr(ord(count)+1)


print("\n\nWrite a program to read a character in uppercase and the print it in lowercase.")
str="WELCOME IN pYthon programming.".lower()
print(str.upper())

print("\n\nWrite a program to swap  two numbers using a temporary variable.")
a=6
b=9
print("Before swap","a=",a,"b=",b)
temp=a
a=b
b=temp
print("After Swap ","a=",a,"b=",b)

print("\n\nWrite a program to demonstrate implicit conversion.")
a=5
b=6
print(a,type(a))
print(b,type(b))
print("The type of the operation performed by both datatype is ",type(b/a))

print("\n\nWrite a program to demonstrate explicit conversion.")
a=5
print("a=",type(a))
print("The type of the a is ",type(float(a)))

print("\n\nWrite a program to read the address of a user .Display the result by breaking it in multiple lines.")
pass

print("\n\nWrite a program to read two floating point numbers.Add these numbers and assign the result to an integer .Finally display the value of all the three variables.")
a,b=5,6
c=float(a+b)
int(c)
print(a,b,c)

print("\n\nWrite  a program to calculate simple intereset and compound interest.")
principle_amount=1000
rate_interest=5/100
time_year=3
simple_interest=(principle_amount*rate_interest*time_year)/100
print("The simple interest was ",simple_interest)

print("\n\nWrite a program that prompts users to enter two integers x and y.The program then calculates and displays x**y.")
a=8
b=3
print("The exponential was ",a**b)
print("\n\nWrite a program that prompts user to enter his first name and last name and the displays a message 'Greetings!!!First name Last name.'")
First_Name,Last_Name="Gavitesh","Patil"
print("'Greetings!!! ",First_Name,Last_Name)

print("\n\nWrite a program that prompts the user to enter the first name and the last name. Then display  the following message.")
print("Hello",First_Name,Last_Name,"\nWelcome to Python!")

print("\n\nWrite a program that calculates number of seconsds in a day.")
a=24*(60*60)
print("The total number of the seconds in the day was ",a)

print("\n\nProgram that accepts an object's mass (in kilograms ) and velocity (in meters per second ) and displays its momentum.")
pass

print("\n\nExersice No.2.")
print("\n\nWrite a program to input two numbers and check whether they are equal or not.")
a,b=23,45
if a==b: print("The numbers is equal .")
else: print("The numbers is not equal .")

print("\n\nWrite a program that prompts users to enter a character (O,A,B,C,F) .Then using if-elif-else construct display Outstanding ,Very good, Good , Average,and Fail respectively.")
user1=["O","A","B","C","F"]
user=user1[Rand.randrange(len(user1))]
print(user)
if user=="O": print("Outstanding")
elif (user=="A"): print("Very Good")
elif (user=="B"): print("Good")
elif (user=="C"): print("Average")
else: print("Fail")

print("\n\nwrite a program that determines whether an alphabet, digit or whitespace was entered.")
digit,alphabet=[x for x in range(9)],[chr(a) for a in range(65,65+26)]
print(digit,alphabet)

print("\n\nWrite a program that determines whether an a;phabet,digit or a whitespace was entered.")
string="l"
if string.isdigit():
    print("The string is contain digit.")
if string.isupper():
    print("The string contain uppercase.")
if string.islower():
    print("The sting contain the lowercase.")

print("\n\nWrite a program that determines whether an alphabet,digit or a whitespace was entered.")
string1="aas"
if string1.isalpha():
    print("The string is alphabet.")
elif string1.isdigit():
    print("The string is digit.")
else:
    print("The string contain whitespace.")


print("\n\nWrite a program that counts the number of lowercase characters,uppercase characters,and digits entered by the user.")
print("For exit from loop enter (-1)")
count1,count2,count3=0,0,0

list3=["l","L","1","3","-1","a"]
while 1:
    user=list3[Rand.randrange(len(list3))]
    if user=="-1":
        print("The loop was stop.")
        break
    elif user.isupper():
        count1+=1
        print("The user input is in uppercase.")
    elif user.islower():
        count2+=1
        print("The user input is in lowercase.")
    elif user.isdigit():
        count3+=1
        print("The user input was digit .")
    else:
        print("Invalid character enter.")
print("The Upper case count was ",count1)
print("The Loweer case count was ",count2)
print("The digit count was ",count3)


print("""Write a program that prompts user to enter a number.
If the number is equal to 99,print "Congratulations".
If the number is less than 99 ,print-- enter again and 
aim higher-else print enter again a lower number .
The program should run until the user guesses the correct the number 
 that is 99.""")