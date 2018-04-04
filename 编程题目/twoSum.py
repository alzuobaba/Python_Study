class Solution(object):
    def twoSum(self,nums,target):
        """
        type nums  :List[int]
        type target :int

        Given an array of integers, return indices of the two numbers such that they add up to a specific target.

        You may assume that each input would have exactly one solution, and you may not use the same element twice.

        Example:
        Given nums = [2, 7, 11, 15], target = 9,

        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].

        """
        num_to_index  = {}
        for i, num in enumerate(nums):
            print(i,num)
            if target - num in num_to_index:
                return [num_to_index[target-num], i]
            num_to_index[num] =i
        return []
s = Solution()
nums = [3,4,7,2,5,8]
result = s.twoSum(nums,5)
print(result)