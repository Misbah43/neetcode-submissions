class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        # Helper function to reverse a portion of the array in-place
        def reverse(l: int, r: int):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1
                
        # 1. Reverse the whole array
        reverse(0, len(nums) - 1)
        # 2. Reverse the first k elements
        reverse(0, k - 1)
        # 3. Reverse the remaining elements
        reverse(k, len(nums) - 1)