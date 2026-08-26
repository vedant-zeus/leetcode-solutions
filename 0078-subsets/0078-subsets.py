class Solution(object):
    def backtrack(self,index , lists , ans , nums , n):
        if index == n:
            ans.append(lists[:])
            return
        
        self.backtrack(index+1,lists,ans,nums,n)
        lists.append(nums[index])

        self.backtrack(index+1,lists,ans , nums ,n)
        lists.pop()

    def subsets(self, nums):
        ans = []
        lists = []

        self.backtrack(0 , lists , ans , nums ,len(nums))

        return ans
        