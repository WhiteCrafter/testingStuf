import plotly.graph_objects as go
import numpy as np
from sklearn.datasets import make_blobs as mb
# Parameters
num_cluster = 6

data_size = 3000
max_iteration = 20  # Adjust for performance; fewer iterations for better performance

# Generate random data
ylist = np.random.random(data_size)
X ,_ = mb(n_samples=data_size, centers=7, cluster_std=1.1, random_state=3)
xlist, ylist = X[:, 0], X[:, 1]
jlist = [[xlist[i], ylist[i]] for i in range(num_cluster)]
centroid_iter = []
clusterlist = [[] for _ in range(num_cluster)]
centroid_list = jlist

# Colors for clusters
fixed_colors =  ["red", "green", "blue", "orange", "purple", "yellow", "pink"]   

# Function to calculate distance
def distance(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Function to calculate average position of points
def avarage(lst):
    length = len(lst[0])
    sum = [0] * length
    for j in range(length):
        for i in lst:
            sum[j] += i[j]
        sum[j] = sum[j] / len(lst)
    min = distance(sum, lst[0])
    mean = lst[0]
    for i in lst:
        if (distance(sum, i )< min):
            min = distance(sum,i)
            mean = i

    return mean

# K-means algorithm
def k_mean():
    global clusterlist
    global centroid_list
    global jlist

# Iterate to find clusters
for i in range(max_iteration):
    centroid_list = jlist
    clusterlist = [[] for _ in range(num_cluster)]
    for j in range(len(xlist)):
        vec = [xlist[j], ylist[j]]
        min = distance(jlist[0], vec)
        min_index = 0
        for k in range(len(jlist)):
            dist = distance(jlist[k], vec)
            if dist < min:
                min = dist
                min_index = k
        clusterlist[min_index].append(vec)
    for j in range(len(jlist)):
        if len(clusterlist[j]) != 0:
            jlist[j] = avarage(clusterlist[j])
    centroid_iter.append((list(centroid_list), list(clusterlist)))  # Store current centroids and clusters

# Create figure with frames
fig = go.Figure()

# Create frames for each iteration
for iter_index, (centroids, clusters) in enumerate(centroid_iter):
    fig.add_trace(go.Scattergl(
        x=[j[0] for j in clusters[0]],  # First cluster
        y=[j[1] for j in clusters[0]],
        mode='markers',
        marker=dict(color=fixed_colors[0], line_width=1),
        name=f"Cluster 1",
        visible= 0# Make the first frame visible initially
    ))

    # Repeat for each cluster
    for c in range(1, num_cluster):
        fig.add_trace(go.Scattergl(
            x=[j[0] for j in clusters[c]],
            y=[j[1] for j in clusters[c]],
            mode='markers',
            marker=dict(color=fixed_colors[c], line_width=1),
            name=f"Cluster {c + 1}",
            visible = 0  # Initially not visible
        ))

    # Add the centroids for this frame
    fig.add_trace(go.Scattergl(
        x=[centroids[c][0] for c in range(num_cluster)],
        y=[centroids[c][1] for c in range(num_cluster)],
        mode='markers',
        marker=dict(color='black', size=15, symbol='x', line_width=2),
        name="Centroids",
        visible=iter_index == 0  # Make the first frame visible initially
    ))

# Create a list of steps for the slider
steps = []
for i in range(max_iteration):
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)},
              {"title": f"Iteration {i + 1}"}],  # Update the title for each step
    )
    # Set the appropriate traces to be visible
    for j in range(num_cluster):
        step["args"][0]["visible"][i * (num_cluster + 1) + j] = True  # Cluster trace
    step["args"][0]["visible"][i * (num_cluster + 1) + num_cluster] = True  # Centroid trace
    steps.append(step)

# Create slider
sliders = [dict(
    active=0,
    currentvalue={"prefix": "Iteration: "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
    sliders=sliders,
    title="K-Means Clustering Animation",
)
fig.show()

