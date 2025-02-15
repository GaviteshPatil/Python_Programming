
arr=[2,4,5,6,6]
arr.remove(max(arr))
print(arr)


x1=2
y1=2
z1=2
N=2

list_array=[[x,y,z] for x in range(x1+1) for y in range(y1+1) for z in range(z1+1)]
def check(lis):
    if sum(lis)!=N:
        return lis
print(list_array)
list_array1=list(filter(check,list_array))
print("Here are your list :- ",list_array1)


import numpy as np 
array1=np.array([[1,2,3],[2,4,6],[3,4,5]])
print(array1)

print("Program to print the given pattern.")
for x in range(8):
    print()
    for j in range(1,x+1):
        print("*",end=" ")


# n=int(input())
# student_marks={}
# for _ in range(n):
#     name,*line=input().split()
#     scores=list(map(float,line))
#     student_marks[name]=scores
# query_name=input()

list123=[9,8,7,6,5,4,44,1,44,3,2,9,8]
list23=sorted(list(set(list123)))
print(list23)
print(list23[1])


list_ex=[]
