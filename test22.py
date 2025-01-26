import matplotlib.pyplot as plt
import numpy as np

r_1 = 1 
c_1 = [-1,1]

def norm_1(x):
    return sum(abs(x[i]**5) for i in range (len(x)))**(1/5)


def distance(a, b, norm):
    return norm([a[i]-b[i] for i in range (len(a))])

def is_in_ball_1(x):
    return distance(x, c_1, norm_1) <= r_1

r_2 = 2
c_2 = [1, 1]

def norm_2(x):
    return max(abs(x[i]) for i in range(len(x)))

def is_in_ball_2(x):
    return distance(x, c_2, norm_2) <= r_2

def is_in_intersection(x):
    return (is_in_ball_1(x) and is_in_ball_2(x))

def visualisze():
    image = [    
    [0 for i in range (100)]  for j in range (100)]

    for i in range(100):    
        for j in range(100):        
            x = j/25 - 2        
            y = -( i/25 - 2)        
            image[i][j] = 0 if is_in_intersection([x,y]) else 1
            
    plt.imshow(image)
    plt.show()

visualisze()