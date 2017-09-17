#code
N=7
moveX=[];
moveY=[];
count=1
queenIndex=[-1]*N
def checkNotAttack(x,y):
    global queenIndex
    for q in queenIndex:
        if(q==-1):
            continue
        xq=q/N
        yq=q%N
        if(x==xq and y==yq):
            return False
        for i in range(len(moveX)):
            if(xq+moveX[i]==x and yq+moveY[i]==y):
                return False
    return True
def createMove():
    for i in range(1,N):
        ##For up and down in same column
        moveX.append(i)
        moveY.append(0)
        moveX.append(-1*i);
        moveY.append(0)
        ###move left and right in same row
        moveX.append(0)
        moveY.append(i)
        moveX.append(0);
        moveY.append(-1*i)
        ###Move diagnally
        moveX.append(i)
        moveY.append(i)
        moveX.append(-1*i);
        moveY.append(-1*i)
        ##Move diagnally
        moveX.append(i)
        moveY.append(-1*i)
        moveX.append(-1*i);
        moveY.append(i)
def printBoard():
    global queenIndex
    print "*******************"
    str1="*"
    for i in range(N*N):
        if i in queenIndex:
            value=1
        else:
            value=0
        str1=str1+str(value)+"  "
        if ((i+1)%N)==0:
            print str1+"*"
            str1="*"
    print "*******************"
def playGame():
    global count, queenIndex
    if count>N:
        return True
    for i in range(N*N):
        nx=i/N
        ny=i%N
        if(checkNotAttack(nx,ny)):
            print "Count:"+str(count)+", Setting queen at "+str(nx)+","+str(ny)
            queenIndex[count-1]=nx*N+ny
            count+=1
            if(playGame()):
                return True
            else:
                count-=1
                queenIndex[count-1]=-1
                print "Count:"+str(count)+", Removing queen at "+str(nx)+","+str(ny)
    return False
if __name__=="__main__":
    createMove()
    if(playGame()):
        printBoard()
    else:
        printBoard()
        print "No solution found"



