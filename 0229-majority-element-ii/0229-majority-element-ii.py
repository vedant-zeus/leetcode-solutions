from collections import defaultdict
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        mpp = defaultdict(int)
        n = len(nums)
        mini = n // 3 + 1

        for num in nums:
            mpp[num] += 1

            if mpp[num] == mini:
                ans.append(num)

        return ans
        