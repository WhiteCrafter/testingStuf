import matplotlib.pyplot as plt
def norm_1(x):    
    return  sum(abs(x[i]) for i in range (len(x)))
def norm_2(x):
    return sum(abs(x[i]**2) for i in range (len(x)))**(1/2)
def norm_inf(x):
    return max(abs(x[i]) for i in range(len(x)))
def norm_generic(x):
    return abs(x[0])+sum(abs(x[i])-abs(x[i-1]) for i in range (1, len(x)))
def distance(a, b, norm):
    return norm([a[i]-b[i] for i in range (len(a))])
def is_in_ball (x, x_0, r, norm):    
    return distance(x, x_0, norm) <= r
image = [    
    [0 for i in range (100)]  for j in range (100)]

for i in range(100):    
    for j in range(100):        
        x = j/25 - 2        
        y = -( i/25 - 2)        
        image[i][j] = 0 if is_in_ball ( [x,y], [1,1], 1, norm_2 ) else 1
        
plt.imshow(image)
plt.show()