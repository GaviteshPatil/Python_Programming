#Syntax for creating the sets :- set_variable = {val1,val2,...}
s={1,2.0,'abc'}
print(s)
print(type(s))
set([1,2.0,'abc'])

#Programming Tip :- If we add the same element multiple times in a set, they are removed because a set cannot have duplicate values.
A=set([1,2,'a','b','def',4.56])
print(A)
print(type(A))

print("\nProgram to create set.\n")
List1=[1,2,3,4,5,6,7,2,3,4,]
print(List1,"contain the duplicates.")

print(set(List1),"its does not contain the duplicate . Set is best data type if you want to avoid the duplicate .")

Tup1=('a','b','c','d','b','e','a')
print(set(Tup1)) #tuple is converted into a set
str2="abcdefabcdefg"
print(set(str2)) #string is converted inot a set

#forms a set of words
print(set("She sells sea shells on the sea shore".split()))

print("Program to find intersection , union ,and symmetric difference between two sets .\n")
coders=set(["Arnav","Goransh","Mani","Parul"])
Analysts=set(["Krish","Mehak","Shiv","Goransh","Mani"])
print("Coders : ",coders)
print("Anlysts : ",Analysts)
print("People working as Coders as well as Analysts : ",coders.intersection(Analysts))
print("People working as Coders or Analysts : ",coders.union(Analysts))
print("People working as Coders but not analysts : ",coders.difference(Analysts))
print("People working as Analysts but not Coders : ",Analysts.difference(coders))
print("People working in only one of the groups : ",coders.symmetric_difference(Analysts))

#Programming Tip:- The update() method can take tuples , lists,strings , or other sets as its argument.

print("\n\nSET OPERATIONS\n\n")
#syntax:- s.update(t)
#description :- Adds elements of set t in the set s provided that all duplicates are avoided 
s=set([1,2,3,4,5])
t=set([6,7,8])
s.update(t)
print(s)

#syntax :- s.add(x)
#description :- Adds element x to the set s provided that all duplicates are avoided
s=set([1,2,3,4,5])
s.add(6)
print(s)

#syntax:- s.remove(x)
#description :- Removes element x from set s.Returns KeyError if x is not present
s=set([1,2,3,4,5])
s.remove(3)
print(s)

#syntax:- s.discard(x)
#description :- Same as remove() but does not give an error if x is not present in the set
s=set([1,2,3,4,5])
print(s)

#syntax:- s.pop()
#description :- Removes and returns any arbitrary element from s.KeyError is raised if s is empty
s=set([1,2,3,4,5])
s.pop()
print(s)

#syntax:- s.clear()
#description:- Removes all elements from the set
s=set([1,2,3,4,5])
s.clear()
print(s)

#syntax:- len(s)
#description:- Returns the length of set
s=set([1,2,3,4,5])

#syntax:- x in s
#description:- Returns True is x is present in set s and False otherwise.
s=set([1,2,3,4,5])
print(3 in s)

#syntax:- x not in s
#description :- Returns True is x is not present in set s and False otherwise
s=set([1,2,3,4,5])
print(6 not in s)

#syntax:- s.issubset(t) or s<=t
#description:- Returns True if every element in set s is present in set t and False otherwise
s=set([1,2,3,4,5])
t=set([1,2,3,4,5,6,7,8,9,10])
print(s<=t)

#syntax:- s.issuperset(t)
#description:- Returns True if every element in t is present in set s and False otherwise.
s=set([1,2,3,4,5])
t=set([1,2,3,4,5,6,7,8,9,10])
print(s.issuperset(t))

#syntax:- s.union(t) or s|t
#description:- Returns a set s that has elements from both sets s and t
s=set([1,2,3,4,5])
t=set([1,2,3,4,5,6,7,8,9,10])
print(s|t)

#syntax:- s.intersection(t) or s&t
#description:- Returns a new set that has elements which are common to both the sets s and t
s=set([1,2,4,3,5,6,7])
t=set([1,2,3,4,5,6,7,8,9,10])
z=s&t
print(z)

#syntax:- s.intersection_update(t)
#description:- Returns a set that has elements which are common to both the sets s and t
s=set([1,2,3,4,5])
t=set([1,2,3,4,5,6,7,8,9,10])
s.intersection_update(t)
print(s)

#syntax:- s.difference(t) or s-t
#description:- Returns a new set that has elements in set s but not in t
s=set([1,2,10,12])
t=set([1,2,3,4,5,6,7,8,9,10,11,12])
z=s-t
print(z)

#syntax:- s.difference_update(t)
#description:- Removes all elements of another set from this set
s=set([1,2,10,12])
t=set([1,2,3,4,5,6,7,8,9,10])
s.difference_update(t)
print(s)


#syntax:- s.symmetric_difference(t) or s^t
#description:- Returns a new set with elements either in s or in t but not both
s=set([1,2,10,12])
t=set([1,2,3,4,5,6,7,8,9,10])
z=s^t
print(z)

#syntax:- s.copy()
#description:- Returns a copy of set s 
s=set([1,2,10,12])
t=set([1,2,3,4,5,6,7,8,9,10])
print(s.copy())

#syntax:- isdisjoint(t)
#description:- Returns True if two sets have a null intersection
s=set([1,2,3])
t=set([4,5,6])
print(s.isdisjoint(t))

#syntax:- all(s)
#description:- Returns True if any of the elements in the set is True .
s=set([0,1,2,3,4])
print(any(s))

#syntax:- enemerate(s) 
#description:- Returns an enumerate object which contain index as well as value of all the items of set as a pair
s=set(['a','b','c','d'])
for i in enumerate(s):
    print(i,end=" ")

#syntax:- max(s)
#description:- Returns the maximum value in a set
s=set([0,1,2,3,4,5])
print(max(s))

#syntax:- min(s)
#description:- Returns the minimum value in a set
s=set([0,1,2,3,4,5])
print(min(s))

#syntax:- sum(s)
#description:- Returns the sum of elments in the set
s=set([0,1,2,3,4,5])
print(sum(s))

#syntax:- sorted(s)
#description:- Retuns a new sorted list from elements in the set .It does not sorts the set as sets are immutable.
s=set([5,4,3,2,1,0])
print(sorted(s))

#syntax:- s==t and s!=t
#description:- s==t returns True if the two set are equivalent and False otherwise s!=t returns True if both sets are not equivalent and False otherwise
s=set(['a','b','c'])
t=set("abc")
z=set([tuple('abc')])
print(s==t)
print(s!=z)

#Note:- A set can be created from a list but a set cannot contain a list.
print("program to iterate through a set")
s=set("hello All,Good Morning")
for i in s:
    print(i,end=" ")

#Note:- To add a single element in the set use the add() method and to add multiple elements in the set ,use the update() method.

print('\nWrite a program that generates a set of prime numbers and another set of odd numbers.Demonstrate the result of union,intersection,difference,and symmetric difference operations on these sets.\n')
def odd(x):
    if x%2==1:
        return x
odd1=list(filter( odd,[x for x in range(1,20)] ))

odd1=list(filter(lambda x: x%2==1,range(1,20)))

odd2=set(odd1)
def prime(x):
    pr=0
    for num in range(2,x):
        if x%num==0:
            pr=1
    if pr==0:
        return x
prime1=set(list(filter(prime,range(1,20))))
print("UNION = ",odd2.union(prime1))
print("INTERSECTION = ",odd2.intersection(prime1))
print("DIFFERENCE = ",odd2.difference(prime1))
print("SYMMETRIC DIFFERENCE = ",odd2.symmetric_difference(prime1))

print(prime1)
print(odd2)

odds=set([x*2+1 for x in range(1,10)])
print(odds)
primes=set()
for i in range(2,20):
    j=2
    flag=0
    while j<i/2:
        if i%j==0:
            flag=1
        j+=1
    if flag==0:
        primes.add(i)
print(primes)
print("UNION :- ",odds.union(primes))
print("INTERSECTION :- ",odds.intersection(primes))
print("SYMMETRIC DIFFERENCE :- ",odds.symmetric_difference(primes))
print("DIFFERENCE :- ",odds.difference(primes))

print("\nWrite a program that creates two sets .One of even numbers in range 1-10 and the other has all composite numbers in range 1-20 .Demonstarte the use all(),issuperset(),len(),and sum() function on the sets.\n")
even=set(list(filter(lambda x : x%2==0,range(1,11))))
print("EVEN = ",even)
def composites(x):
    com=0
    for num in range(2,x):
        if x%num==0:
            com=1
    if com==1:
        return x 
composites1=set(list(filter(composites,range(1,20))))
print(composites1)

print("COMPOSITES :",composites1)
print("SUPERSET :- ",even.issuperset(composites1))
print("ALL : ",all(even))
print("LENGTH OF COMPOSITES SET : ",len(composites1))
print("SUM OF ALL NUMBERS IN EVENS SET : ",sum(even))

print("\nWrite a program that creates two sets - squares and cubes in range 1-10.Demonstrate tha use of update(),pop(),remove(),add() and clear() functions.\n")
cubes=set(list(map(lambda a: a**3,range(1,11))))
squraes=set(list(map(lambda a: a**2,range(1,11))))

cube=set([x**2 for x in range(1,11)])
square=set([x**3 for x in range(1,11)])
print("SQUARES : ",square)
print("CUBES : ",cube)
print("UPDATE : ",square)
square.add(11**2)
square.add(11**3)
print("ADD : ",square)
print("POP : ",square.pop())
square.remove(1331)
print("REMOVE : ",square)
square.clear()
print("CLEAR : ",square)

print("\n\nWrite a program that has a list of countries .Create a set of the countries and print the names of the countries in sorted order.\n")
countries=['India','Russia','China','Brazil','England']
C_set=sorted(set(countries))
print(C_set)