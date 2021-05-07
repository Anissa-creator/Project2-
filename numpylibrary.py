# Anissa Champion
#numpy library example

import numpy as np 
# Array 1
arr= np.array([[15,18],[23,44]])
# Array 2
arr2= np.array([[20,78],[19,56]])
#add two arrays
sum= np.add(arr,arr2)
print("Addition of Two Arrays: ")
print(sum)

me=np.mean(arr2)
print("The mean is :" )
print(me)  

x=np.delete(arr,1)
print ("after deletion array becomes")
print (x)