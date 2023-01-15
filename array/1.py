class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i, n in enumerate(nums):
            to_find = target - n
            if to_find in hash_map.keys():
                return [hash_map[to_find], i]
            else:
                hash_map[n] = i
        return
        

nums = [3, 2, 4]
target = 6
sl = Solution()
print(sl.twoSum(nums, target))