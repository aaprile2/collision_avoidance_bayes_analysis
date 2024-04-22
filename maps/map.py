import numpy as np
import matplotlib.pyplot as plt
from typing import List


class Map():
    """ Helper class for creating, visualizing, and displaying 
        maps for simulation.
    """
    def __init__(self):
        # Initialize with an binary array
        # (0 = path, 1 = obstacle)
        self.map = None
    
    def set_map(self, map: List):
        # Set map using a list of lists of binary values
        self.map = np.array(map)
        return self.map
    
    def load_map(self, path):
        # Load map from Numpy file
        self.map = np.load(path)
        return self.map
    
    def save_map(self, path):
        # Save map to Numpy file
        np.save(path, self.map)
        return

    def display(self):
        # Plot map
        plt.imshow(~self.map, cmap='gray')

    def get_obstacle_ratio(self):
        # Compute the ratio of obstacle area to total map area
        return len(np.where(self.map == 1)[0]) / np.prod(self.map.shape)
    
    def image_to_cartesian(self):
        # Convert the path (0) and obstacle (1) pixel coordinates to
        # Cartesian coordinates
        cartesian_coords = dict()
        for i in [0, 1]:
            coords_y, coords_x = np.where(self.map == i)
            coords = np.stack([coords_x, coords_y], axis=1)
            coords[:, 1] = (len(self.map)) - coords[:, 1]
            cartesian_coords[i] = coords
        
        return cartesian_coords
    

