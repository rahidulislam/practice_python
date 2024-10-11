class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # if len(nums) >=2:
        #     for num in nums:
        #         next_position = nums.index(num) + 1
        #         if next_position <= len(nums)-1:
        #             if num + nums[next_position] == target:
        #                 return [nums.index(num), next_position]
        #         else:
        #             return []
        # else:
        #     return []
        # position = 0
        # while len(nums) >= 2 and position < len(nums)-1:
        #     next_position = position+1
        #     if nums[position] + nums[next_position] == target:
        #         return [position, next_position]
        #     position += 1

        # for num in nums:
        #     next_num = target - num
        #     # if next_num is not num:
        #     new_list = nums.copy()
        #     new_list.remove(num)
        #     if next_num in new_list:
        #         return [nums.index(num), nums.index(next_num)]
        #     return []

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

        found = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in found:
                return [found[compliment], i]
            found[nums[i]] = i
        return []   
s = Solution()
# print(s.twoSum([2,7,11,15],9))
# print(s.twoSum([3,2,3],6))
print(s.twoSum([3,3],6))
# print(s.twoSum([2,5,4,3,9],6))