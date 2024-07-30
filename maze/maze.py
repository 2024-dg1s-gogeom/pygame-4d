import numpy as np
import pygame

class Maze:
    n = int(input("Enter the size of Tesseract(size of thes side)"))
    def __init__(self, n):
        self.pos = np.array([0, 0, 0, 0])
        self.size = n

    def generate_coords(self, n):
        grid = np.indices((n+1, n+1, n+1, n+1))
        coords = np.stack(grid, axis=-1).reshape(-1,4)
        coords_list = coords.tolist()
        return coords_list
    
    def generateMaze(self, n):
        path = [[[[0 for x in range(n)] for y in range(n)] for z in range(n)] for w in range(n)] # 0: 막힌 길, 1: 뚫린 길, 2: 시작점, 3: 도착점

        # 길 생성 알고리즘. 이 부분은 임의로 수정 가능 (일단 지금은 가장 기초적인 모델)
        for i in range(n):          
            path[i][0][0][0] = 1
        for j in range(n):
            path[n-1][j][0][0] = 1
        for k in range(n):
            path[n-1][n-1][k][0] = 1
        for w in range(n):
            path[n-1][n-1][n-1][w] = 1

        # 도착지잠 / 시작지점 결정 알고리즘
        path[0][0][0][0] = 2
        path[n-1][n-1][n-1][n-1] = 3


