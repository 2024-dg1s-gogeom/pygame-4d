class Maze():
    def __init__(self, n):
        self.maze = [[[[[i, j, k, l] for l in range(n)] for k in range(n)] for j in range(n)] for i in range(n)]
        self.pos = [0, 0, 0, 0]
        self.size = n
        self.path = NewPath() # from [0,0,0,0] to [n-1,n-1,n-1,n-1]
