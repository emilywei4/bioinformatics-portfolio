import sys
from typing import List, Dict, Iterable, Tuple

def point_distance(pt1, pt2): #helper function to calculate the distance between two points
    """
    Calculate the Euclidean distance between two points.
    """
    distance = sum((pt1[i] - pt2[i]) ** 2 for i in range(len(pt1))) ** 0.5
    return distance

def farthest_first_traversal(k: int, m: int, data: List[Tuple[float, ...]]) -> List[Tuple[float, ...]]:
    """
    Perform the Farthest First Traversal algorithm on the given data.
    """
    centers = [data[0]] #pick random center (whichever point comes first in data)
    while len(centers) < k: #keep looping until we have our desired number of centers
        maxDist = -1 #initialize max distance
        farthestPt = None #initialize farthest point

        for point in data: #loop through all points in data
            minDist = float('inf') #initialize min distance
            for center in centers: 
                distance = point_distance(point, center) #compute distance from current point to center
                if distance < minDist:
                    minDist = distance #find smallest distance to any center

            if minDist > maxDist: #check if min dist is the largest we've seen
                maxDist = minDist #set max dist to new min dist
                farthestPt = point #store point at max distance

        centers.append(farthestPt) #when we find the point that is farthest from its closest list of centers, we add to centers

    return centers
