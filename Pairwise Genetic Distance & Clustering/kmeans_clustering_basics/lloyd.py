from typing import List, Tuple

def point_distance(pt1, pt2): #helper function to calculate the distance between two points
    """
    Calculate the Euclidean distance between two points.
    """
    distance = sum((pt1[i] - pt2[i]) ** 2 for i in range(len(pt1))) ** 0.5
    return distance

def find_centers(clusters: List[List[Tuple[float, ...]]], m: int) -> List[Tuple[float, ...]]: #helper function to calculate the mean of each cluster (center)
    """
    Compute centers for each cluster. 
    """
    centers = [] #initialize return list of centers
    for cluster in clusters: #for each cluster
        if cluster: #if cluster is nonempty
            center = tuple(sum(point[i] for point in cluster) / len(cluster) for i in range(m)) #calculate the mean of all points in cluster
            centers.append(center) #add as a center to list of centers
    return centers

def lloyd(k: int, m: int, data: List[Tuple[float, ...]]) -> List[Tuple[float, ...]]:
    """
    Implement Lloyd's algorithm for k-means clustering.
    """
    centers = data[:k] #choose first k points to be the initial centers
    prevCenters = None #keep track of previous iteration's centers to see if they change

    while prevCenters != centers: #keep iterating until there is no change in the locations of the centers
        clusters = [[] for _ in range(k)] #initialize k lists (one for each cluster) 
        for point in data: #iterate through points
            distances = [point_distance(point, center) for center in centers] #compute distance from center to each point
            closestIndex = distances.index(min(distances)) #finds index closest to center
            clusters[closestIndex].append(point) #add point to its nearest cluster

        prevCenters = centers #save old centers as previous centers for next iteration
        centers = find_centers(clusters, m) #recalculate centers for next iteration

    return centers
