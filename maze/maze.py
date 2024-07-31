import numpy as np
import pygame

class Maze:
    ##### 맵 시작 알고리즘 #####
    global tesseractSize; tesseractSize = 20
    global mazePath; mazePath = [[[[0 for x in range(tesseractSize)] for y in range(tesseractSize)] for z in range(tesseractSize)] for w in range(tesseractSize)] 
    # 0: 막힌 길, 1: 뚫린 길, 2: 시작점, 3: 도착점

    def __init__(self, tesseractSize):
        self.pos = np.array([0, 0, 0, 0])
        self.size = tesseractSize

    def generate_coords(self, tesseractSize):
        grid = np.indices((tesseractSize+1, tesseractSize+1, tesseractSize+1, tesseractSize+1))
        coords = np.stack(grid, axis=-1).reshape(-1,4)
        coords_list = coords.tolist()
        return coords_list
    
    ##### 길 생성 알고리즘 #####
    def generateMaze(self, tesseractSize):

    ### 가장 기초적인 길 모델 (추후 임의로 수정 가능) ###
        for i in range(tesseractSize):          
            mazePath[i][0][0][0] = 1
        for j in range(tesseractSize):
            mazePath[tesseractSize-1][j][0][0] = 1
        for k in range(tesseractSize):
            mazePath[tesseractSize-1][tesseractSize-1][k][0] = 1
        for w in range(tesseractSize):
            mazePath[tesseractSize-1][tesseractSize-1][tesseractSize-1][w] = 1

    ### 시작지점, 도착지점 결정 ###
        mazePath[0][0][0][0] = 2
        mazePath[tesseractSize-1][tesseractSize-1][tesseractSize-1][tesseractSize-1] = 3


