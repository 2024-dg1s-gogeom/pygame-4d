import numpy as np
import pygame
import random as r

class Maze:
    ##### 맵 시작 알고리즘 #####
    global mazePath; mazePath = [[[[0 for x in range(22)] for y in range(22)] for z in range(22)] for w in range(22)] 
    # 0: 막힌 길, 1: 뚫린 길, 2: 시작점, 3: 도착점

    def __init__(self):
        self.pos = np.array([0, 0, 0, 0])
        self.size = 20

    def generate_coords(self):
        grid = np.indices((21, 21, 21, 21))
        coords = np.stack(grid, axis=-1).reshape(-1,4)
        coords_list = coords.tolist()
        return coords_list
    
    def mazeMode():
        global modeOfMaze
        modeOfMaze = input("Random or Stated? (r/s): ")

    ##### 랜덤 미로 생성 -> 깊이 우선 탐색(DFS) 알고리즘 이용, 미로크기 홀수배로 해야 오류안나더라고요 21x21x21x21로 설정했습니다 #####
    
    global startRmazeX, startRmazeY, startRmazeZ, startRmazeW
    startRmazeX = r.randrange(1,21,2)
    startRmazeY = r.randrange(1,21,2)
    startRmazeZ = r.randrange(1,21,2)
    startRmazeW = r.randrange(1,21,2)
    
    def randomMaze():
        ### 시작지점 설정 ###
        mazePath[startRmazeX][startRmazeY][startRmazeZ][startRmazeW] = 2

        ### 도착지점 설정 ###
        while True:
            endX = r.randrange(1,21,2)
            endY = r.randrange(1,21,2)
            endZ = r.randrange(1,21,2)
            endW = r.randrange(1,21,2)

            if (endX, endY, endZ, endW) != (startRmazeX, startRmazeY, startRmazeZ, startRmazeW):
                break
        
        mazePath[endX][endY][endZ][endW] = 3

        ### 시작지점, 도착지점 최단경로 생성 ###
        visit = [(startRmazeX, startRmazeY, startRmazeZ, startRmazeW)] # 방문한 셀 기록
        direction = [
            (0,0,-2,0), (0,0,2,0),
            (0,-2,0,0), (0,2,0,0),
            (-2,0,0,0), (2,0,0,0),
            (0,0,0,-2), (0,0,0,2)
        ] # 방향 설정

        while visit:
            x, y, z, w = visit[-1]
            neighbor = []

            # 이웃 셀 탐색
            for dx, dy, dz, dw in direction:
                nx, ny, nz, nw = x+dx, y+dy, z+dz, w+dw
                if (
                    0 < nx < 21 and 0 < ny < 21 and 0 < nz < 21 and 0 < nw < 21 and
                    mazePath[nx][ny][nz][nw] == 0
                ):
                    neighbor.append((nx, ny, nz, nw))

            # 무작위 이웃 셀 선택
            if neighbor:
                nx, ny, nz, nw = r.choice(neighbor)
                mazePath[(y+ny) // 2][(x+nx) // 2][(z+nz) // 2][(w+dw) // 2] = 1
                mazePath[nx][ny][nz][nw] = 1
                visit.append((nx, ny, nz, nw))
            else:
                visit.pop()
        
    ##### 정해진 미로 (랜덤미로에 오류가 있을 시) #####
    def statedMaze():
        for x in range(0,10):  mazePath[x][0][0][0]    = 1 # (0,0,0,0) -> (9,0,0,0)
        for y in range(0,4):   mazePath[9][y][0][0]    = 1 # (9,0,0,0) -> (9,3,0,0)          
        for x in range(9,13):  mazePath[x][3][0][0]    = 1 # (9,3,0,0) -> (12,3,0,0)          
        for w in range(0,6):   mazePath[12][3][0][w]   = 1 # (12,3,0,0) -> (12,3,0,5)
        for z in range(0,8):   mazePath[12][3][z][5]   = 1 # (12,3,0,5) -> (12,3,7,5)
        for y in range(3,9):   mazePath[12][y][7][5]   = 1 # (12,3,7,5) -> (12,8,7,5)
        for z in range(4,8):   mazePath[12][8][z][5]   = 1 # (12,8,7,5) -> (12,8,4,5)
        for w in range(5,12):  mazePath[12][8][4][w]   = 1 # (12,8,4,5) -> (12,8,4,11)
        for x in range(10,13): mazePath[x][8][4][11]   = 1 # (12,8,4,11) -> (10,8,4,11)
        for w in range(11,20): mazePath[12][8][4][w]   = 1 # (12,8,4,11) -> (12,8,4,20)
        for x in range(12,16): mazePath[x][8][4][20]   = 1 # (12,8,4,20) -> (15,8,4,20)
        for z in range(4,11):  mazePath[15][8][z][20]  = 1 # (15,8,4,20) -> (15,8,10,20)
        for w in range(14,20): mazePath[15][8][10][w]  = 1 # (15,8,10,20) -> (15,8,10,14)
        for y in range(8,16):  mazePath[15][y][10][14] = 1 # (15,8,10,14) -> (15,15,10,14)
        for z in range(10,20): mazePath[15][15][z][14] = 1 # (15,15,10,14) -> (15,15,20,14)
        for x in range(15,20): mazePath[x][15][20][14] = 1 # (15,15,20,14) -> (20,15,20,14)
        for y in range(15,20): mazePath[20][y][20][14] = 1 # (20,15,20,14) -> (20,20,20,14)
        for w in range(14,20): mazePath[20][20][20][w] = 1 # (20,20,20,14) -> (20,20,20,20)

        mazePath[0][0][0][0] = 2
        mazePath[20][20][20][20] = 3

    mazeMode()
    if modeOfMaze == 'r': randomMaze()
    elif modeOfMaze == 's': statedMaze()
    else: print("error!")

    