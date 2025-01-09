# Hive
Hive – The next generation spatial index

## Overview
Hive is a novel spatial indexing data structure designed for efficient storage, querying, and management of spatial objects in 2D or 3D space. Inspired by the natural structure of a beehive, it combines grid-based partitioning with hierarchical local trees (like KD-trees) to achieve superior performance in both dynamic and static datasets. Hive offers faster insertions, optimized queries, and scalability compared to traditional spatial indexing techniques like R-trees.

This repository provides the Python implementation of Hive, along with benchmarking tools, usage examples, and detailed comparisons to existing spatial index solutions.

## Features
1. Grid-Based Partitioning: Divides space into fixed-size cells for rapid object lookup.
Dynamic Local Structures: Uses hierarchical tree structures for efficient querying within cells.
2. Fast and Scalable: Combines O(1) grid-based insertion with O(log m) intra-cell querying.
3. Customizable Design: Fully adjustable grid size, hierarchical tree type, and splitting strategies.

## Applications
1. Geographic Information Systems (GIS)
2. Medical data storage
3. Robotics and Autonomous Navigation
4. Spatial Databases and Big Data Analytics
5. Gaming and Virtual Reality
6. IoT and Sensor Network Data Management

## Installation
```
git clone git@github.com:AjeyPaiK/hive.git
cd hive
pip install requirements.txt
```
## Usage

```
from hive import HybridSpatialIndex, SpatialObject

# Initialize the spatial index
beehive = HybridSpatialIndex(x_range=(0, 100), y_range=(0, 100), grid_size=10)

# Add spatial objects
beehive.insert(SpatialObject(id=1, coordinates=(15, 15)))
beehive.insert(SpatialObject(id=2, coordinates=(35, 45)))

# Query objects within a radius
results = beehive.query((20, 20), radius=10)
print([obj.id for obj in results])
```
## Benchmarking
```
cd hive
python benchmark.py
```
## Complexity Analysis

This section provides a detailed comparison of the **Hive** data structure against the traditional R-tree in terms of complexity for common operations.

| Operation        | R-tree Complexity           | Hive Complexity                              |
|------------------|-----------------------------|---------------------------------------------|
| **Insertion**    | O(log n)                   | O(1) for grid lookup + O(log m) for KD-tree |
| **Point Query**  | O(log n)                   | O(1) for grid lookup + O(log m) for KD-tree |
| **Range Query**  | O(√n + k)                  | O(c + k), where c = number of neighbor cells accessed |
| **Memory Usage** | Moderate (tree overhead)   | Higher for sparse datasets due to grid overhead |

### Key Terms

- **n**: Total number of objects in the dataset.
- **m**: Number of objects in a single grid cell.
- **k**: Number of results returned by a query.
- **c**: Number of neighboring cells accessed during a range query.

### Insights

- **Insertion Efficiency**: Hive benefits from a constant-time grid lookup, making it faster than R-tree for dynamic datasets.
- **Query Performance**:
  - For **dense queries** (small regions), R-tree performs better due to fewer bounding box checks.
  - For **sparse queries** (large regions), Hive outperforms R-tree due to reduced traversal requirements.
- **Memory Usage**: Hive requires more memory than R-tree for sparse datasets because of the overhead introduced by the grid structure.
- **Scalability**: Hive is ideal for 2D or 3D datasets but may require optimization for high-dimensional data where R-tree retains an edge.

### Use Cases

- **Hive** is particularly suited for:
  - Real-time applications requiring fast insertions and localized queries.
  - Applications with non-uniform data distributions.
- **R-tree** is better for:
  - High-dimensional datasets.
  - Applications where dense spatial queries dominate.


