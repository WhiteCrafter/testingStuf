import numpy as np

def vectorSum(a, b):
    c = []
    for i in range(0, len(a)):
        c.append(a[i] + b[i])
    return c

print (vectorSum([1,2], [4,5]))

def dotProduct(a,b):
    c = 0
    for i in range(0,len(a)):
        c += a[i] * b[i]
    return c
def scalar(vec, scal): 
    for i in range(0, len(vec)):
        vec[i] = vec[i] * scal
    return vec
    
def matrixSum(a,b):
    c = [[]]
    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            c[i][j] = a[i][j] + b[i][j]
    return c

