def program25():
    #program to display the  number.
    num1 = int(input("Enter the nth number \n>>>"))
    i = 0
    while num1 > i:
        print(i)
        i += 1


def program26():
    #program to print the value in horizontal row.
    num1 = int(input("Enter the nth number \n>>>"))
    i = 0
    while num1 > i:
        print(i, end=" ")
        i += 1


def program27():
    #program to find the sum and average of the number.
    i = 0
    s = 0
    while i <= 10:
        s += i
        i += 1
    print("The sum of the number is " + str(s))
    print("Average of the number is " + str(float(s) / 10))


def program28():
    #program to display the asterisk(*).
    i = 0
    while i <= 20:
        print("*", end=" ")
        i += 1


def program29():
    #program to display the sum of the number.
    m = int(input("Enter the 'm' number \n>>>"))
    n = int(input("Enter the 'n' number \n>>>"))
    m1 = m
    sum1 = 0
    while m <= n:
        sum1 += m
        m += 1
    print("THE SUM OF " + str(m1) + 'TH' + " AND " + str(n) + 'TH IS ' + str(sum1))


def program30():
    #program to read the numbers until -1 is encountered.Also count the negativies,positive and zerors entered by the user.
    negative = positive = zeros = 0
    while True:
        num = int(input("Enter the number \n>>>"))
        if num == -1:
            print("THANKS FOR YOUR UNVALUEABLE TIME.")
            break
        elif num < 0:
            negative -= 1
        elif num > 0:
            positive += 1
        else:
            zeros += 1
    print("THE TOTAL POSITIVE NUMBER IS " + str(positive))
    print("THE TOTAL NEGATIVE NUMBER IS " + str(negative))
    print("THE TOTAL ZEROS    NUMBER IS " + str(zeros))


def program31():
    #program to check wherathere the number is Amstrong number or not.
    num1 = int(input("Enter the number:- \n>>>>"))
    num2 = 0
    num3 = 0
    while num1 > 0:
        num2 = num1 % 10
        num3 = num3 + (num2 ** 3)
        num1 /= 10
    if num3 == num1:
        print(str(num1) + " is the Armstrong number.")
    else:
        print("The number is not Armstrong number.")


def program32():
    #program to read a character until a* is encountered . Also count the number of uppercase, lowercase, and numbers entered by the users.
    count_upper = 0
    count_lower = 0
    count_num = 0
    cha = input("Enter any charcter \n>>>")
    while cha != '*':
        cha = input("Enter any charcter \n>>>")
        if cha >= "0" and cha <= "9":
            count_num += 1
        elif cha >= "A" and cha <= "Z":
            count_upper += 1
        else:
            count_lower += 1
    print("The count of lower number is " + str(count_lower))
    print("The count of upper number is " + str(count_upper))
    print("The count of number is " + str(count_num))


def program33():
    #program to display the sum of the ENter digits 
    num1 = int(input("Enter the number:- \n>>>"))
    num2 = 0
    while num1 > 0:
        reminder = num1 % 10
        num2 = num2 + reminder
        num1 /= 10
    print("The sum of the digits is " + str(int(num2)))


num=19989
n=0
while num!=0:
    n=(n*10)+(num%10)
    num=num//10
print("The reversed number is "+str(n))

