import numpy as np
import pygame

class Maze():
    n = int(input("Enter the size of Tesseract(size of thes side)"))
    def __init__(self, n):
        self.pos = [0, 0, 0, 0]
        self.size = n

    def generate_coords(self, n):
        grid = np.indices((n+1, n+1, n+1, n+1))
        coords = np.stack(grid, axis=-1).reshape(-1,4)
        return coords
        # self.path = self.NewPath() # from [0,0,0,0] to [n-1,n-1,n-1,n-1]
    
    def NewPath():
        pass

    def Update(list):
        charPos = [0,0,0,0]
        charPos += list