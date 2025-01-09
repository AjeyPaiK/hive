from rtree import index
import time
import numpy as np
from hive import HybridSpatialIndex, SpatialObject

# Create an R-tree index
r_tree = index.Index()

# Generate random 2D points
num_points = 10000
points = [(i, (np.random.uniform(0, 100), np.random.uniform(0, 100))) for i in range(num_points)]

# Insert points into R-tree
start_time = time.time()
for i, (x, y) in points:
    r_tree.insert(i, (x, y, x, y))  # R-tree requires bounding boxes
r_tree_insertion_time = time.time() - start_time

# Perform a range query
query_box = (20, 20, 50, 50)
start_time = time.time()
results_rtree = list(r_tree.intersection(query_box))
r_tree_query_time = time.time() - start_time

# Using the previously defined HybridSpatialIndex class
hybrid_index = HybridSpatialIndex(x_range=(0, 100), y_range=(0, 100), grid_size=10)

# Insert points into Hybrid Spatial Index
start_time = time.time()
for i, (x, y) in points:
    hybrid_index.insert(SpatialObject(id=i, coordinates=(x, y)))
hybrid_insertion_time = time.time() - start_time

# Perform a range query
start_time = time.time()
results_hybrid = hybrid_index.query((35, 35), radius=15)  # Simulating a range query
hybrid_query_time = time.time() - start_time

print(f"r_tree query time: {r_tree_query_time}")
print(f"r_tree insertion time: {r_tree_insertion_time}")
print(f"hive query time: {hybrid_query_time}")
print(f"hive insertion time: {hybrid_insertion_time}")
