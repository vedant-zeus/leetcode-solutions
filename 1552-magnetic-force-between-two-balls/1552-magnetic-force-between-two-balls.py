class Solution(object):
    def canweplace(self,position,dist,balls):
        n = len(position)
        cntballs = 1 
        last = position[0]

        for i in range(1,n):
            if position[i] - last >= dist :
                cntballs += 1

                last = position[i]

            if cntballs >= balls:
                return True
        return False

    def maxDistance(self, position, m):

        n = len(position)
        position.sort()
        low = 1
        high = position[n-1] - position[0]

        while low <= high:
            mid = (low + high)//2
            if self.canweplace(position,mid,m):
                low = mid + 1
            else:
                high = mid - 1
        return high 
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        