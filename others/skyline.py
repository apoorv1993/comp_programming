#https://leetcode.com/problems/the-skyline-problem/description/
import heapq,collections
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        critical=collections.OrderedDict() ##key is critical point= [height,[left=0!right=1,index of rectangle]]
        height=[] ##[height,pointer index]
        points=[]*len(buildings)
        activeBuilding={}
        i=0
        for L,R,H in buildings:
            points.append([L,R,H])
            if L in critical:
                critical[L][1].append([0,i])
            else:
                critical[L]=[0,[[0,i]]]
            if R in critical:
                critical[R][1].append([1,i])
            else:
                critical[R]=[0,[[1,i]]]
            i+=1
        critical=collections.OrderedDict(sorted(critical.items()))
        print str(critical)
        for key,cPoint in critical.iteritems():
            for p in cPoint[1]:
                if p[0]==0:#Left
                    heapq.heappush(height,[points[p[1]][2]*-1,p[1]])
                    activeBuilding[p[1]]=1
                else: ##Right
                    del activeBuilding[p[1]]
            while True:
                try:
                    heightP=heapq.heappop(height)
                except:
                    break
                if heightP[1] not in activeBuilding:
                    continue
                else:
                    cPoint[0]=heightP[0]*-1
                    heapq.heappush(height,heightP)
                    break
        result=[]
        prevH=0
        for key,value in critical.iteritems():
            if value[0]==prevH:
                continue
            result.append([key,value[0]])
            prevH=value[0]
        print str(result)
        return result
            
            
            
        