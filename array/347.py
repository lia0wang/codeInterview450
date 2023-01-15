class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == len(nums):
            return nums

        hash_map = {}
        for n in nums:
            hash_map[n] = nums.count(n)
        
        # sort items: 4:1, ..., key is the criterial of the sorting
        # in this case: key will be the item.key for each item
        sorted_hash_map = dict(sorted(hash_map.items(), key=lambda x: x[1]))
        return [x for x in sorted_hash_map.keys()][-k:]
        
nums = [1,1,1,2,2,3, -1, -1,-1, -1, -2,-2,-2,-2,0,0,0]
k = 3
sl = Solution()
print(sl.topKFrequent(nums, k))
