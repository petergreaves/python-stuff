import numpy as np

c = np.empty(5, float)
c[0] = 1.3
c[1] = c[0] + 3.1
#print (c)

z = np.zeros(5, float)
#print (z)


#
myList = [1.9, 7.1, 4.6, 3.2, 1.9]
ex1_2array = np.array(myList)
# zero-indexing
print("The second element is", str(ex1_2array[1]))
print("The number of elements is", str(len(ex1_2array)))
print("The sum of the elements is", str(sum(ex1_2array)))