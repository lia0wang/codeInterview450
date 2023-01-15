class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # memo = []
        # for n in nums:
        #     memo.append(n)
        #     if memo.count(n) > 1:
        #         return True
        # return False
        
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False
        

nums_1 = [1,1,1,3,3,4,3,2,4,2]
nums_2 = [1,2,3,4]

solution = Solution()
print(solution.containsDuplicate(nums_1))
print(solution.containsDuplicate(nums_2))
