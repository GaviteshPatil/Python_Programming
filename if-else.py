def program11():
    #program to determinne wheathere a person is eligible for vote or not.
    age=int(input("Enter the age of candidate \n:-"))
    if age>18:
        print("Eligible for vote.")
    else:
        print("The year for eligibility is",(18-age))

def program12():
    #program to find grater number between two number.
    num1=int(input("Enter the first number \n>>>"))
    num2=int(input("Enter the second number \n>>>"))
    if num1>num2:
        print("The number "+str(num1)+" is greater than "+str(num2))
    else:
        print("The number "+str(num2)+"is greater than "+str(num1))

def program13():
    #program to covert input characters into upper and lower case simultenously.
    chr=input("Enter a spelling \n>>> ")
    if(chr>"A"and chr<"Z"):
        print("The charcters is in uppercase its lowercase is ",chr.lower())
    else:
        print("THe chracter is in lowercase ,Uppercase is ",chr.upper())

def program14():
    #program to calculate the bonus and salary of the employees.
    sal=int(input("| Enter the salary of employee |\n>>> "))
    se=input("| Enter the sex or gender of employee(m or f ) |\n>>>")
    if se=="m":
        bonus=0.05*sal
    else:
        bonus=0.10*sal
    amount=sal+bonus
    print("***********************")
    print("Salary =\t",sal)
    print("Bonus = \t",bonus)
    print("***********************")
    print("Total salary =\t",amount)

def program15():
    #program to display the interval of between the number.
    num1=int(input("Enter a number who's interval you want to display \n=>"))
    if(num1<30 and num1>0):
        print("The number is between the range of the 0-30 .")
    if(num1<60 and num1>30):
        print("The number is between the range of the 30-60 .")
    if(num1<80 and num1>60):
        print("The number is between the range of the 60-80 .")
    if(num1<100 and num1>80):
        print("The number is between the range of the 80-100 .")

def program16():
    #program to the check wheather the number is positive or negative.
    num2=int(input("Enter the number \n>>>"))
    if num2 == 0 :  
        print("The number is zero.")
    elif( num2>0):
        print("The number is positive number.")
    else:
        print("The number is negative number.")

def program17():
    #program to display the input alphabet is vowel or not.
    chr=input("Enter the alphabet \n>>>")
    if(chr=='A' or chr=='E' or chr=='I' or chr =='O' or chr =='U'):
        print("The alphabet is vowel .")
    elif(chr=='a' or chr=='e' or chr=='i' or chr=='o'or chr == 'u'):
        print("The alphabet is vowel.")
    else:
        print("The alphabet is not vowel.")

def program18():
    #program to findout the greatest number between three number.
    nun5=int(input("Enter the first number \n>>>"))
    nun6=int(input("Enter the second number \n>>>"))
    nun7=int(input("Enter the three number \n>>>"))
    if(nun5>nun6 and nun5>nun7):
        print("The ",str(nun5),"is greater than "+str(nun6)+" and "+str(nun7))
    elif(nun6>nun5 and nun6>nun7):
        print("The ",str(nun6),"is greater than "+str(nun5)+" and "+str(nun7))
    else:
        print("The ",str(nun7),"is greater than "+str(nun5)+" and "+str(nun6))

def program19():
    #program to display the days by input the number.
    print('''Following are the list of days and number for display the day by recogenize the number 1-7  
    "Monday" = "1"
    "Tuesday" = "2"
    "Wednesday" = "3"
    "Thursday" = "4"
    "Friday" = "5"
    "Saturday" = "6"
    "Sunday" = "7"
    ''')
    days=input("Enter the number(1 to 7)\n >>>>")
    if(days=='1'):
        print("Your selected day is 'Monday'.")
    elif(days=='2'):
        print("Your selected day is 'Tuesday'.")
    elif(days=='3'):
        print("Your selected day is 'Wednesday'.")
    elif(days=='4'):
        print("Your selected day is 'Thursday'.")
    elif(days=='5'):
        print("Your selected day is 'Friday'.")
    elif(days=='6'):
        print("Your selected day is 'Saturday'.")
    elif(days=='7'):
        print("Your selected day is 'Sunday'.")
    else:
        print("Invalid number,Check number in the list.")
def program20():
    #program to display the days according to books
    days=int(input("Enter the number between 1-7 \n>>>"))
    if(days==7):print("its a sunday.")
    elif(days==1):print("its a monday.")
    elif(days==2):print("its a tuesday.")
    elif(days==3):print("its a wednesday.")
    elif(days==4):print("its a thursday.")
    elif(days==5):print("its a friday.")
    elif(days==6):print("its a saturday.")
    else:print("Check the number.")

def program21():
    #program to calculate the tax by recognizening income.
    income=int(input("Enter a income amount \n >>>"))
    min1=150001
    min2=300000
    max1=300001
    max2=500000
    max3=500001
    tax=0.10
    tax2=0.20
    tax3=0.30
    taxeable_income=income-150001
    if(taxeable_income==0):print("no tax.")
    elif(taxeable_income>min1 or taxeable_income<min2):
        print("Your tax is "+str(float(taxeable_income-min1)*tax))
    elif(taxeable_income>max1 or taxeable_income<max2):
        print("Your tax is "+str(float(taxeable_income-max1)*tax2))
    else:
        print("Your tax is "+str(float(taxeable_income-max3)*tax3))

def program23():
    #progtam to determine the character input by user is number or alphabet (Uppercase or lowercase).
    chr=input("Enter the character \n>>>")
    if((chr>='A')and(chr<='Z')):
        print("The character is alphabet in uppercase .")
    elif((chr>='a')and(chr<='z')):
        print("The charcter is alphabet in lowercase .")
    elif(int(chr)>=0 and int(chr)<=10):
        print("The character is number.")
    else:
        print("Its a not a alphabet or number.")

#programe to calculate the grade of the student and distrubute it accordings to its grade.
def program22():
    print("*******************Marksheet*******************")
    mark1=int(input("|  The mark in first  subject      | "))
    mark2=int(input("|  The mark in second subject      | "))
    mark3=int(input("|  The mark in third  subject      | "))
    mark4=int(input("|  The mark in fourth subject      | "))
    total_mark=400
    percentage=int(((mark1+mark2+mark3+mark4)/400)*100)
    if(percentage>75):
        grade="Distinction"
    elif(percentage>60 and percentage<=75):
        grade="First grade"
    elif(percentage>50 and percentage<=60):
        grade="Second grade"
    elif(percentage>40 and percentage<=50):
        grade="Third grade"
    else:
        grade="Fail"
    print("_______________________________________________")
    print("|  TOTAL MARKS                     |  ",(mark1+mark2+mark3+mark3+mark4))
    print("|  PERCENTAGE                      |  ",percentage)
    print("|  GRADE                           |  ",grade)

#program to determine the roots.
def program30():
    a=int(input("Enter the value of a\t>>> "))
    b=int(input("Enter the value of b\t>>> "))
    c=int(input("Enter the value of c\t>>> "))
    a2=2*a
    D=(b*b)-(4*a*c)
    formula=D/a2
    print("The value of \"formula method\" is "+str(formula))
    if D>0 :
        print("Its a Real root.")
        root1=(-b + (D**0.5))
        root2=(-b - (D**0.5))
        print("The root1 and root2 of the equation is "+str(root1)+" and "+str(root2))
    elif D == 0:
        print("Its a Unimaginary root.")
        root1=-b/a2
        print("The root1 and root2 of equation is "+str(root1))
    else:
        print("IMAGINARY ROOTS .")

program22()