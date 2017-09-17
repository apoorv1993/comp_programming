'''
A Maze is given as N*N binary matrix of blocks where source block is the upper left most block i.e., maze[0][0] and destination block is lower rightmost block i.e., maze[N-1][N-1]. A rat starts from source and has to reach destination. The rat can move only in two directions: forward and down.
In the maze matrix, 0 means the block is dead end and 1 means the block can be used in the path from source to destination. Note that this is a simple version of the typical Maze problem. For example, a more complex version can be that the rat can move in 4 directions and a more complex version can be with limited number of moves.
'''
#code
N=4
moveX=[-1,0];
moveY=[0,-1];
sol=[[0]*N]*N
def checkLimits(board,x,y):
    if(x<0 or y <0 or x>=N or y>=N or board[x][y]!=1):
        return False
    else:
        return True
def playGame(board,x,y):
    if x==0 and y==0:
        return True ##Reached Destination
    for i in range(len(moveX)):
        nx=x+moveX[i]
        ny=y+moveY[i]
        if(checkLimits(board,nx,ny)):
            print "Moved from x:"+str(x)+",y:"+str(y)+" to X:"+str(nx)+",Y=:"+str(ny)
            sol[nx][ny]=1
            if(playGame(board,nx,ny)):
                return True
            else:
                print "Backtracked to x:"+str(x)+",y:"+str(y)+" from X:"+str(nx)+",Y=:"+str(ny)
                sol[nx][ny]=0
        else:
            print "Move not allowed from x:"+str(x)+",y:"+str(y)+" to X:"+str(nx)+",Y=:"+str(ny)
    return False
if __name__=="__main__":
    x=(N-1)
    y=N-1
    print str(sol)
    sol[x][y]=1 ##Starting point of RAT
    board=[[1, 0, 0, 0],[1, 1, 0, 1],[0, 1, 0, 0],[1, 1, 1, 1]]
    print str(sol)
    if(playGame(board,x,y)):
        print str(sol)
    else:
        print str(sol)
        print "No solution found"

        
        
