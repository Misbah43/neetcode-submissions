class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        # Initialize min_len to infinity so any valid length will be smaller
        min_len = float('inf')
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # While our window satisfies the condition, shrink from the left to find the minimum
            while current_sum >= target:
                current_window_len = right - left + 1
                min_len = min(min_len, current_window_len)
                
                # Shrink the window
                current_sum -= nums[left]
                left += 1
                
        # If min_len was never updated, it means no valid subarray was found, return 0
        return min_len if min_len != float('inf') else 0
        