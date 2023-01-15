class Solution:
    def findKthSmallest(self, nums, k: int) -> int:
        # nums.sort(reverse=True)
        # return nums[k-1]
        n = len(nums)

        def partition(l, r, pivot):
            pivot_ele = nums[pivot]
            nums[r], nums[pivot] 
            
        def quick_select(l, r, k):
            if l == r: return nums[l]
            
            pivot_index = partition(l, r, l)
    
        
        return quick_select(0, n-1, k)

nums = [2, 4,1, 5, 6, 77, 231, 231]
sl = Solution()
print(sl.findKthSmallest(nums, 3))