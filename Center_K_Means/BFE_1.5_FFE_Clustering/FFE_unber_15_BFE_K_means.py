import os
import math
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def Haversine_matrix_distance(origin, destination): #found here https://gist.github.com/rochacbruno/2883505
    lat1, lon1 = origin[0],origin[1]
    lat2, lon2 = destination[0],destination[1]
    radius = 6371 # km
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c
    return d

def find_euclidian_distance(xycoor1, xycoor2):
    """Return Euclidian distance between two (x, y) coordinates."""
    d_sq = (xycoor2[0] - xycoor1[0]) ** 2 + (xycoor2[1] - xycoor1[1]) ** 2
    return math.sqrt(d_sq)


def find_total_distance(xlist, ylist, labels, centroids):
    """Return total distance between xy and centroid, prints centroid count."""
    centroids_count = []
    for _ in centroids:
        centroids_count.append(0)

    # import pdb; pdb.set_trace()
    xylist = list(zip(xlist, ylist))

    total_distance = 0
    for xycoor, c_index in zip(xylist, labels):
        centroid_coor = centroids[c_index]
        centroids_count[c_index] += 1
        # total_distance += find_euclidian_distance(xycoor, centroid_coor)
        total_distance += Haversine_matrix_distance(xycoor, centroid_coor)

    print(centroids_count)
    return total_distance


MIN_CLUSTERS = 4
MAX_CLUSTERS = 9

# Read in location data and weights
# cols = ['x', 'y', 'weight']
# data = pd.read_csv('location_data.csv', names=cols)

# cols=['target_lat', 'target_lon', 'FFE_elevation_ft']

data = pd.read_csv(r'F:\A_CUHK\DTM_HK\Galveston_K_Means_FFE_BFE\BFE_1.5_FFE_Cluster'
                   r'ing\need_ele_above_1_5ft_Gal_cost_FFE_2022_6_10.csv')

xcoor0 = data.target_lat.tolist()
ycoor0 = data.target_lon.tolist()

xcoor = data.target_lat.tolist()
ycoor = data.target_lon.tolist()
weights = data.FFE_elevation_ft.tolist()

# Adjust x and y coors for weights
# Weights are interpreted like frequency
for i, wt in enumerate(weights):
    for _ in range(1, int(wt)):
    # for _ in range(1, wt):
        xcoor.append(xcoor[i])
        ycoor.append(ycoor[i])

data = {'x': xcoor, 'y': ycoor}
df = pd.DataFrame(data, columns=['x', 'y'])

if not os.path.exists('results'):
    os.mkdir('results')
# Iterate through different num_clusters
for num_clusters in range(MIN_CLUSTERS, MAX_CLUSTERS + 1):
    kmeans = KMeans(n_clusters=num_clusters).fit(df)
    centroids = kmeans.cluster_centers_

    # Write centroid info
    with open(f'results/N={num_clusters}-centroids.csv', 'w') as fout:
        fout.write('CENTROID COORDINATES:\n')
        fout.write('centroid_num, x, y\n')
        for i, c in enumerate(centroids):
            fout.write(f'{i}, {round(c[0], 3)}, {round(c[1], 3)}\n')

    # Write client info
    with open(f'results/N={num_clusters}-results.csv', 'w') as fout:
        fout.write('CLIENT COORDINATES AND CENTROID NUMBER\n')
        fout.write('x, y, centroid_no\n')
        for x, y, n in zip(xcoor0, ycoor0, kmeans.labels_[0:len(xcoor0) - 1]):
            # fout.write(f'{round(x, 3)}, {round(y, 3)}, {n}\n')
            fout.write(f'{round(x, 6)}, {round(y, 6)}, {n}\n')

    # Save clusters plot
    # plt.scatter(df['x'], df['y'], c=kmeans.labels_.astype(float), s=50, alpha=0.5)
    plt.scatter(df['x'], df['y'], c=kmeans.labels_.astype(float), s=50, alpha=0.2)
    # plt.savefig(f'results/N={num_clusters}-grouped.png')

    # Save clusters with centroids plot
    # plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=30)
    plt.savefig(f'results/N={num_clusters}-grouped-with-center.png')
    plt.close()

    total_distance = find_total_distance(xcoor0, ycoor0, kmeans.labels_[0:len(xcoor0) - 1], centroids)
    print(total_distance)
