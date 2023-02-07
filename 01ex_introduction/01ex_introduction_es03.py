import math
import numpy as np
import scipy.linalg as la

def euclideanDistance(p1, p2):
    print("The distance between these two points is: ")
    print(math.sqrt(pow(p1[0]-p2[0],2)+pow(p1[1]-p2[1],2)))

p1 = (3,0)
p2 = (0,4)


a = np.array(p1)
b = np.array([p2[0], p2[1]])

print(la.norm(a-b))

euclideanDistance(p1,p2)
