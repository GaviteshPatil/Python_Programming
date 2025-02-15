#normal data type
x=complex(1,2)
print(x)

y=["apple","Banana","cherry"]
print(tuple(y))

j=range(6)
print(list(j))

#list operation 
"Note :- its mutable, Ordered, Allows duplicate"
#operation of the list at beginner level

my_list=[1,2,3,'apple','banana']
print(my_list[2])

a=my_list.copy()
print(a)

my_list.remove("banana")
print(my_list)

my_list.append('venom')
print(my_list)

my_list.pop()
print("here the output of the pop funtion")
print(my_list)

print(my_list.count(2))


#intermediate operation on the list
print(len(my_list))
print(my_list[1:4])

#list comprehension
squares=[x**2 for  x in range(6)]
print(squares)

#sorting of the list


#Advanced operation on the list
nested_list = [[1,2,3],[4,5,6]]
print(nested_list[1][2])

my_list.extend([7,8])
print(my_list)
print(len(my_list))

my_list = [1,2,3,4,5]
square=tuple(map(lambda x:x**2, my_list))
even = list(filter(lambda x: x%2 == 0, my_list))
print(square)
print(even)

"""
SET:-  A set is an unordered collection of unique items. 
Sets are mutable """
#beginner level operation on set data type
my_set = {1,2,3,'apple'}



my_set.remove('apple')
print(my_set)

my_set.add("1")
print(my_set)

#intermediate operatons on set 

set_a={1,2,3}
set_b={3,4,5}


print(f"The union of the set {set_a | set_b}") #Union
print(f"The intersection of the set {set_a & set_b}") #Intersecton 
print(f"The Difference of the set {set_a - set_b}") #Difference
print(f"The Summertic Difference of the set {set_a ^ set_b}") #Summetric Difference

#set comprehension
square_set = {x**2 for x in range(7) if x%2==0}
print(square_set)

#Advanced operation on set
print("Advanced Operation on set".upper())

#Frozen Set
frozen =frozenset([1,2,3])
print(frozen)

#Advanced set methods
sebset = {1,2,3,4,5,6,7}
print(sebset.issubset(set_a))

print(set_a.issuperset(sebset))
print(sebset.issuperset(set_a))
print(set_a.issubset(sebset))

my_tuple = (1,2,3,'apple')
print(my_tuple[1])

#Intermediate operation on the tuple
print(my_tuple[1:3])

#unpacking tuples
a,b,c,d =my_tuple
print(a,b,c,d)

print("Advanced operation On set".capitalize())

nested_tuple = ((1,2),(3,4))
print(nested_tuple[1][1])

#tuple method and function
print(len(my_tuple))
print(my_tuple.index("apple"))

print("Dictionary and its operation".swapcase())

#Creating a Dictionary
my_dict = {'name':"Ishwer",'age':25}

# Accessing Elements
print(my_dict["name"])

# adding/updating elements
my_dict['city'] = 'New York'
print(my_dict)

del my_dict['age']
print(my_dict)

# Intermediate Operations
for key, value in my_dict.items():
    print(f"{key}:{value}")

# Dictinary Comprehension
Square = {x:x**2 for x in range(5)}
print(Square)

# Nested Dictionaries
nested_dict= {
    'person':{
        "name":'Alice',
        "age":25
    }
}
print(nested_dict)

#Advanced Dictionary Methods
# Using get with a default value

print(my_dict.get('age','Unknown'))

#Merging dictionaries
dict_a ={"a":1,"b":2}
dict_b ={"b":3,"c":4}
merged_dict ={**dict_a,**dict_b}
print(merged_dict)

