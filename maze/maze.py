import numpy as np
import pygame
import random as r

class Maze:
    ##### 맵 시작 알고리즘 #####
    global mazePath; mazePath = [[[[0 for x in range(21)] for y in range(21)] for z in range(21)] for w in range(21)] 
    # 0: 막힌 길, 1: 뚫린 길, 2: 시작점, 3: 도착점

    def __init__(self):
        self.pos = np.array([0, 0, 0, 0])
        self.size = 20

    def generate_coords(self):
        grid = np.indices((21, 21, 21, 21))
        coords = np.stack(grid, axis=-1).reshape(-1,4)
        coords_list = coords.tolist()
        return coords_list

    ### 시작지점, 도착지점 인수 돌리기 ###
    global startPos; startPos = r.randrange(20)
    endPos = r.randrange(20)

    ### 시작지점, 도착지점 최단경로 생성 ###
    for x in range(startPos,20): mazePath[x][0][0][0] = 1
    for y in range(20): mazePath[19][y][0][0] = 1
    for z in range(20): mazePath[19][19][z][0] = 1
    for w in range(endPos): mazePath[19][19][19][w] = 1

    ### 시작지점, 도착지점 결정 ###
    mazePath[startPos][0][0][0] = 2
    mazePath[19][19][19][endPos] = 3

    # ##### 길 생성 알고리즘 #####
    # ### 길 모델 (추후 임의로 수정 가능) ###
    # for x in range(0,10): # (0,0,0,0) -> (9,0,0,0)          
    #     mazePath[x][0][0][0] = 1
    # for y in range(0,4): # (9,0,0,0) -> (9,3,0,0)          
    #     mazePath[9][y][0][0] = 1
    # for x in range(9,13): # (9,3,0,0) -> (12,3,0,0)          
    #     mazePath[x][3][0][0] = 1
    # for w in range(0,6): # (12,3,0,0) -> (12,3,0,5)
    #     mazePath[12][3][0][w] = 1
    # for z in range(0,8): # (12,3,0,5) -> (12,3,7,5)
    #     mazePath[12][3][z][5] = 1
    # for y in range(3,9): # (12,3,7,5) -> (12,8,7,5)
    #     mazePath[12][y][7][5] = 1
    # for z in range(4,8): # (12,8,7,5) -> (12,8,4,5)
    #     mazePath[12][8][z][5] = 1
    # for w in range(5,12): # (12,8,4,5) -> (12,8,4,11)
    #     mazePath[12][8][4][w] = 1
    # for x in range(10,13): # (12,8,4,11) -> (10,8,4,11)
    #     mazePath[x][8][4][11] = 1
    # for w in range(11,20): # (12,8,4,11) -> (12,8,4,19)
    #     mazePath[12][8][4][w] = 1
    # for x in range(12,16): # (12,8,4,19) -> (15,8,4,19)
    #     mazePath[x][8][4][19] = 1
    # for z in range(4,11): # (15,8,4,19) -> (15,8,10,19)
    #     mazePath[15][8][z][19] = 1
    # for w in range(14,20): # (15,8,10,19) -> (15,8,10,14)
    #     mazePath[15][8][10][w] = 1
    # for y in range(8,16): # (15,8,10,14) -> (15,15,10,14)
    #     mazePath[15][y][10][14] = 1
    # for z in range(10,20): # (15,15,10,14) -> (15,15,19,14)
    #     mazePath[15][15][z][14] = 1
    # for x in range(15,20): # (15,15,19,14) -> (19,15,19,14)
    #     mazePath[x][15][19][14] = 1
    # for y in range(15,20): # (19,15,19,14) -> (19,19,19,14)
    #     mazePath[19][y][19][14] = 1
    # for w in range(14,20): # (19,19,19,14) -> (19,19,19,19)
    #     mazePath[19][19][19][w] = 1
