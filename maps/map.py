import numpy as np
import matplotlib.pyplot as plt
from typing import List

class Map():
    def __init__(self):
        self.map = None
    
    def set_map(self, map: List):
        self.map = np.array(map)
        return self.map
    
    def load_map(self, path):
        self.map = np.load(path)
        return self.map
    
    def save_map(self, path):
        np.save(path, self.map)
        return

    def display(self):
        plt.imshow(~self.map, cmap='gray')

    def get_obstacle_ratio(self):
        return len(np.where(self.map == 1)[0]) / np.prod(self.map.shape)
    
    def image_to_cartesian(self):
        cartesian_coords = dict()
        for i in [0, 1]:
            coords_y, coords_x = np.where(self.map == i)
            coords = np.stack([coords_x, coords_y], axis=1)
            coords[:, 1] = (len(self.map)) - coords[:, 1]
            cartesian_coords[i] = coords
        
        return cartesian_coords
    

