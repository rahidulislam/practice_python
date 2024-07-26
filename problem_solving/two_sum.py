class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        found = []
        for num in nums:
            y = target - num
            if y in nums:
                if nums.index(num) in found 
                found.extend([nums.index(num), nums.index(y)])
        return found

s = Solution()
print(s.twoSum([2,7,11,15],9))
