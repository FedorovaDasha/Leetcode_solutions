class Solution(object):
    @staticmethod
    def two_sum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_nums = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in dict_nums:
                return [dict_nums[difference], index]
            dict_nums[num] = index
        return None
