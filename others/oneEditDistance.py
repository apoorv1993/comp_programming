#https://leetcode.com/problems/one-edit-distance/description/
class Solution(object):
    def updateDistance(self,s,t,m,n,alreadyIncremented=0):
        if m==0:
            return n
        if n==0:
            return m
        if s[m-1]==t[n-1]:
            return self.updateDistance(s,t,m-1,n-1,alreadyIncremented)
        else:
            if alreadyIncremented==1:
                return 2
            return 1+ min(self.updateDistance(s,t,m-1,n-1,1),self.updateDistance(s,t,m,n-1,1),self.updateDistance(s,t,m-1,n,1)) 
    def isOneEditDistance(self, s, t):
        m,n=len(s),len(t)
        if self.updateDistance(s,t,m,n,0)==1:
            return True
        else:
            return False        
        