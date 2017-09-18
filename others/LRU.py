#https://leetcode.com/problems/lru-cache/description/
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.count=0
        self.capacity=capacity
        self.items={}
        self.deque=collections.deque()
    def updateLRU(self,key):
        if key in self.deque:
            self.deque.remove(key)
        self.deque.append(key)
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.items:
            self.updateLRU(key)
            #print "After get:"+str(self.deque)
            return self.items[key]
        else:
            return -1
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.items:
            self.items[key]=value
            self.updateLRU(key)
            return
        if self.count==self.capacity:
            #print "Limit reached"
            while True:
                item=self.deque.popleft()
                if item in self.items:
                    del self.items[item]
                    break
        else:
            self.count+=1
        self.updateLRU(key)
        self.items[key]=value
        #print "After put deque:"+str(self.deque)+", items:"+str(self.items)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)