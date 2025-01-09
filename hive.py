import numpy as np
from scipy.spatial import KDTree

class SpatialObject:
    def __init__(self, id, coordinates):
        self.id = id
        self.coordinates = np.array(coordinates)

class GridCell:
    def __init__(self):
        self.objects = []
        self.tree = None

    def insert(self, obj):
        self.objects.append(obj)
        self.tree = KDTree([o.coordinates for o in self.objects])

    def query(self, point, radius=None):
        if self.tree is None:
            return []
        if radius is None:
            return self.tree.query(point)
        else:
            return self.tree.query_ball_point(point, radius)

class HybridSpatialIndex:
    def __init__(self, x_range, y_range, grid_size):
        self.x_min, self.x_max = x_range
        self.y_min, self.y_max = y_range
        self.grid_size = grid_size
        self.cells = {}
        self._initialize_grid()

    def _initialize_grid(self):
        x_cells = int((self.x_max - self.x_min) / self.grid_size)
        y_cells = int((self.y_max - self.y_min) / self.grid_size)
        for i in range(x_cells):
            for j in range(y_cells):
                self.cells[(i, j)] = GridCell()

    def _get_cell_key(self, point):
        x, y = point
        i = int((x - self.x_min) / self.grid_size)
        j = int((y - self.y_min) / self.grid_size)
        return (i, j)

    def insert(self, obj):
        key = self._get_cell_key(obj.coordinates)
        self.cells[key].insert(obj)

    def query(self, point, radius=None):
        key = self._get_cell_key(point)
        results = []
        for neighbor_key in self._get_neighbors(key):
            if neighbor_key in self.cells:
                results.extend(self.cells[neighbor_key].query(point, radius))
        return results

    def _get_neighbors(self, key):
        i, j = key
        neighbors = [
            (i + dx, j + dy) for dx in range(-1, 2) for dy in range(-1, 2)
        ]
        return neighbors
