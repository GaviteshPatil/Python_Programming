import numpy as np

#The core of Numpy is its ndarray object, which represents an n-dimensional array.


"""NumPy (Numerical Python) is a powerful Python library used for numerical and scientific computing.
It provides support for arrays , matrices , and many high-level matahmatical functions to operate on these data structure efficiently."""

print("\nCreating arrays from list")
#Creating a 1D array 
arr = np.array([1,2,3,4,5])
print(arr)

#Creating a 2D array (matrix)
arr_2d = np.array([[1,2],[3,4],[5,6]])
print(arr_2d)

arr_2d1=np.array([[1,2,3],[4,5,6]])
print(arr_2d1)

print("\nBasic Array Operations.")
#Element-wise Operations
print("You can perform operations on the entire array at once without writing loops.")

arr = np.array([1,2,3])

#Multiply each element by 2
result = arr * 2
print(result)

#Similarly , you can do
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

#Element-wise addition
result = arr1 +arr2
print(result)

print("\n Mathematical Functions.")
arr = np.array([0,np.pi/2,np.pi])

#Apply sine function to each element 
result = np.sin(arr)
r2=np.cos(arr)
print(result)
print(r2)

print("\nArray Shape and Reshaping.")
#Checking the Shape of an Array.
"""The shape of an array tells you its dimensions. For example , a 2x3 matrix has 
a shape of (2,3). """

arr_2d = np.array([[1,2],[3,4],[5,6]])
print(arr_2d.shape)

#Reshaping an Array
"""You can change the shape of an array using reshape()."""

arr = np.array([1,2,3,4,5,6])

#Reshape into a 2x3 matrix
reshaped_arr=arr.reshape(2,3)
print(reshaped_arr)

#Array Indexing and Slicing
"""You can access elements of a NumPy array similar to how you do with Python lists."""

#Indexing
arr = np.array([10,20,30,40])

#Access the first element
print(arr[0])

#For multi-dimensional arrays:
arr_2d = np.array([[1,2],[3,4],[5,6]])

#Access the element at the first row, second column
print(arr_2d[0,1])

#Slicing 
"""You can slice arrays to access subarrays."""

arr = np.array([10,20,30,40,50])

#Get elements from index 1 to 3 (exclusive)
print(arr[1:3])

"For multi-dimensional arrays."
arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

#Get the first two rows
print(arr_2d[:2,:])

#Useful NumPy Functions.

"Zeros and Ones Arrays"
"You can create arrays filled with zeros or ones."

#Array of zeros
zeros_arr=np.zeros((3,3))
print(zeros_arr)

#Array of ones
ones_arr = np.ones((2,4))
print(ones_arr)

#Arange and Linspace
" np.arange(start,stop,step) : Similar to Python's range(),it creates arrays with a range of numbers."

#Array with numbers from 0 to 9
arr = np.arange(10)
print(arr)

"np.linspace(start,stop,num) : Creates an array with evenly spaced numbers between start and stop."

#Array with 5 equally spaced numbers between 0 and 1
arr = np.linspace(0,1,5)
print(arr)

#Sum, Min, Max, and Mean
"NumPy provides convenient functions to calculate basic staistics "

arr = np.array([1,2,3,4,5])

#Sum of all elements
print(np.sum(arr))

#Minimum and maximum
print(np.min(arr))
print(np.max(arr))

#mean(average)
print(np.mean(arr))

#Broadcasting 
"""Broadcasting allows NumPy to perform operations on arrays of different shapes.
This avoids writing complex loops and makes oprations more efficient."""

arr = np.array([1,2,3])

#Add 10 to each element
result = arr + 10
print(result)

#Random Numbers 
"You can generate random numbers with NumPy's random module"

#Random integers between 0 and 10
random_integers = np.random.randint(0,10,size=(3,3))
print(random_integers)

#Random floats between 0 and 1
random_floats = np.random.random((3,3))
print(random_floats)

"""
Summary of Key Concepts:
Arrays: NumPy provides arrays (ndarray), which are more efficient and faster than Python lists.

Operations: You can perform element-wise operations, apply mathematical functions, and use broadcasting.

Shape and Reshaping: Check and change the shape of arrays easily.

Indexing/Slicing: Access or modify elements using indexing and slicing.

Useful Functions: NumPy offers many useful functions like zeros(), ones(), arange(), sum(), etc."""



"Below program is used to do the Scalar Math on each element in the array." 

#Program to demonstrate the operation on the array 
arr2= np.array([23,45,67])
#addition
print(np.add(arr2,1))  #Add 1 to each array element

#subratation 
print(np.subtract(arr,10)) #Subtract 10 from each array element

#multiplication
print(np.multiply(arr,20)) #multiply each array element by 20

#Divide
print(np.divide(arr2,4))  #Divide each array element by 4 (returns np.nan for division by zero)

#Powerth to each element of array
print(np.power(arr2,5)) #Raise each array element to the 5th power.
      
"Below programs is used to do the Statistics math by using the numpy."

arr4=np.array([23,43,21,56])

print(np.mean(arr4,axis=0)) #Returns mean along specific axis
print(arr_2d.sum()) #Returns sum of arr
print(arr4.min())       #Returns minimum value of arr
print(arr.max(axis=0))   #Returns maximum value of specific axis

print(np.var(arr4))    #Returns the variance of array
print(np.std(arr,axis =0))    #Returns the standard deviation of specific axis
print(np.corrcoef(arr4))   #Returns correlation coefficient of array



"Below programs operation is used to calculate the Vector Math."
print(np.add(arr1,arr_2d))   #Elementwise add arr_2d to arr1
print(np.subtract(arr1,arr_2d))   #Elementwise subtract arr2 from arr_2d 
print(np.multiply(arr,arr_2d1))   #Elementwise multiply arrby arr_2d1
print(np.divide(arr,arr_2d1))   #Elementwise  divide arr1 by arr2
print(np.power(arr1,arr_2d1))   #Elementwise raise arr1 raised to the power of arr_2d1
print(np.array_equal(arr1,arr1))
print()
print(np.array_equal(arr1,arr_2d)) #Returns True if the arrays have the same elements adn shape

print(np.sqrt(arr4))  #Square root of each elemetn in the array
print(np.sin(arr_2d1))   #Sine of each element in the array
print(np.log(arr_2d)) #Natural log of each element in the array
print(np.abs(arr_2d))  #Absolute value of each element in the array
print(np.floor(arr_2d))   #Rounds down to the nearest int
print(np.ceil(arr_2d)) #Rounds up to the nearest int
print(np.round(arr_2d))  #Rounds to the nearest int
