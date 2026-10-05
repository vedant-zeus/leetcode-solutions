class Solution(object):

    def partitions(self,nums, maxsum):
        n = len(nums)
        partition = 1
        subarray = 0

        for i in range( n):
            if subarray + nums[i] <= maxsum:
                subarray += nums[i]
                
            else:
                partition +=1
                subarray = nums[i]
        return partition

    def splitArray(self, nums, k):

        low = max(nums)
        high = sum(nums)

        while low <= high :
            mid = (low + high) // 2
            partition = self.partitions(nums,mid)

            if partition > k :
                low = mid + 1

            else:
                high = mid - 1
        return low 