class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []

        for index, value in enumerate(nums):
            index_lst = [x for x in range(0, len(nums))]
            index_lst.remove(index)
      
            res = 1
            for i in index_lst:
                res *= nums[i]

            result.append(res)
        return result
            

nums = [-1,1,0,-3,3]
sl = Solution()
print(sl.productExceptSelf(nums))