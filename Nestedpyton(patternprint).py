#program to print the specific pattern by using the python programming
for x in range(1,6):
        print("PASS",str(x),"=",end=" ")
        for j in range(1,6):
            print(j,end=" ")
        print()

#program to print the specific pattern no. 2 by using the nested for loop.
for x in range(1,6):
    print("P\na\ns\ns\n",str(x),"= ")
    for j in range(1,6):
        print(str(j))
    print()
#program to print the specific pattern no.3 by using the nested for loop.
for x in range(1,6):
    print()
    for j in range(1,6):
        print("*",end="")