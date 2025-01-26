import plotly.graph_objects as go
import numpy as np
import plotly.express as px

num_cluster = 3
data_size = 1000
max_iteration = 1000

xlist =  np.random.randn(data_size)
ylist = np.random.randn(data_size)
jlist = [[xlist[i], ylist[i]] for i in range(num_cluster)]
centroid_iter = []
clusterlist = [[] for _ in range(num_cluster)]

colorlist = [""]*1000

fixed_colors = ["red", "green", "blue", "orange", "purple", "yelow"]

def distance(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def avarage(list):
    length = len(list[0])
    sum = [0]*length
    for j in range(length):   
        for i in list:  
            sum[j] += i[j]
        sum[j] = sum[j]/len(list)
    return sum

def k_mean():
    global clusterlist
    clusterlist= [[] for _ in range(num_cluster)]
    for j in range(len(xlist)):
        vec = [xlist[j], ylist[j]]
        min = distance(jlist[0], vec)
        min_index =0
        for k in range(len(jlist)):
            dist = distance(jlist[k], vec)
            if(dist < min): 
                min = dist
                min_index = k
        clusterlist[min_index].append(vec)
    for j in range(len(jlist)):
        if (len(clusterlist[j]) !=0):
            jlist[j] = avarage(clusterlist[j])


for i in range(max_iteration):
    k_mean()
    centroid_iter.append(jlist)
       
fig = go.Figure()

for i, cluster in enumerate(clusterlist):
    print("trace" + str(i))
    print(len(cluster))
    fig.add_trace(go.Scattergl(
        x = [j[0] for j in cluster],
        y = [j[1] for j in cluster],
        mode = 'markers',
        marker=dict(
        color = fixed_colors[i],
        line_width=1
        ),
        name = ("cluster" + str(i+1))
    ))

xl = [j[0] for j in jlist]
yl = [j[1] for j in jlist]
fig.add_trace(go.Scattergl(
    x = xl,
    y = yl,
    mode='markers',
    marker=dict(color='black',  # Set a distinct color for the cluster centers
        size=15,        # Make the centers larger
        symbol='x',     # Use a different marker symbol (optional)
        line_width=2
    )
))
fig.show()
