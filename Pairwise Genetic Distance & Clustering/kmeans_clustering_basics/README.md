# K-means Clustering Basics

**Problem**  
How can we choose initial centers, quantify clustering quality, and iteratively refine clusters for k-means?

**Approach**  
This set includes the three core building blocks of k-means:
- `farthest_first_traversal.py` — greedy seeding that spreads centers apart (maximizes minimum distance).
- `squared_error_distortion.py` — average squared distance from each point to its nearest center (clustering “loss”).
- `lloyd.py` — classic Lloyd’s algorithm: assign → recompute centers → repeat until stable.

---

## Files & Key Functions

- `farthest_first_traversal.py`  
  - `point_distance(pt1, pt2)`  
  - `farthest_first_traversal(k, m, data) -> List[Tuple[float,...]]`
- `squared_error_distortion.py`  
  - `squared_error_distortion(k, m, centers, data) -> float`
- `lloyd.py`  
  - `point_distance(pt1, pt2)`  
  - `find_centers(clusters, m)`  
  - `lloyd(k, m, data) -> List[Tuple[float,...]]`

---

## Usage

```python
# Example 2D dataset
points = [(1.0,1.0),(1.5,2.0),(3.0,4.0),(5.0,7.0),(3.5,5.0),(4.5,5.0),(3.5,4.5)]

# 1) Farthest-first seeding
from farthest_first_traversal import farthest_first_traversal
init_centers = farthest_first_traversal(k=2, m=2, data=points)

# 2) Distortion
from squared_error_distortion import squared_error_distortion
dist = squared_error_distortion(k=2, m=2, centers=init_centers, data=points)

# 3) Lloyd's k-means
from lloyd import lloyd
final_centers = lloyd(k=2, m=2, data=points)
