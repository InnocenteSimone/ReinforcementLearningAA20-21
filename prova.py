import numpy as np


matrix = np.random.randint(10,size=(5,10))

print(matrix)
print("\n")
print(matrix[2,:])
print("\n")
print(np.argmax(matrix[2,:]))