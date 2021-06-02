import numpy as np

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

#converting the list to an array using numpy
myArray = np.array(my_list)

#Shaping the array
# 1. Below is 2 dimensional Array 
# & both lines give same result 
arr1_v1 = myArray.reshape(len(my_list),1)
#or
arr1_v2 = myArray.reshape(-1,1)  

# 2. below is another example
arr2 = myArray.reshape(3,5)

#---------------------------------------------------------------
print("List : {}".format(my_list))
print("Array : {}".format(myArray))
print("Reshaped Array: {}".format(arr1_v1))
print("Reshaped Array: {}".format(arr1_v2))
print("Reshaped Array : {}".format(arr2))

#below tells dimension of the array
#print(arr2.ndim)