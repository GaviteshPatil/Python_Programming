player=False
while(player==False):
    print("Welcome ,in the game of 'playing with numbers")
    mode=input('''
    Select your mode
    #list of numbers = 1
    #Reversed the numbers = 2
    #Sum of numbers = 3
    #Sum of digits = 4
    #Factorial of n numbers = 5
    "Enter your mode number " = 
    ''')
    
    if(mode=="1"):
        i=input("Enter your type of number 'even' or 'odd'= ")
        if(i=='even'):
            num=int(input("Enter your number= "))
            i=0
            while(i<=num):
                if(i==0):
                    print("The even number is",i)
                i+=1
                if(i%2==0):
                    print("The even number is",i)
                else:
                    continue
            else:
                print("Above numbers is  even numbers")
        elif(i=="odd"):
            num=int(input("Enter your numbers:- "))
            i=0
            while(i<=num):
                i+=1
                if(i%2==1):
                    print("The odd number is",i)
                else:
                    continue
            else:
                print("Above numbers is  odd numbers")
        else:
            print("invaild spelling,Check your spelling.")

    elif(mode=="3"):#sum of n number
        num=int(input("Enter a number= "))
        sum=0
        i=1
        while i<=num:
            sum+=i
            i+=1
        print("The sum of number of",num,"is",sum)
    elif(mode=="5"):  #factorial of n number 
        num=int(input("Enter a number:- "))
        i=1
        fact=1
        while i<=num:
            fact=fact*i
            i+=1
        print("The factorial of ",num,"is",fact)
    
    elif(mode=="3"):#sum of digits
        num=int(input("Enter your number:- "))
        sum = 0
        while(num>0):
            a=num%10
            sum+=a
            num//=10
        print("The sum of digits is ",sum)
    elif(mode=="2"):#reversed the digits
        num=int(input("Enter the number:- "))
        reverse=str("The reaverse value is ")
        while(num>0):
            a=num%10
            reverse+=str(a)
            num//=10
        print(reverse)
    else:
        print("Invalid number, Check a number.")