class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return True
            
            # Handle duplicates where we can't determine the sorted half
            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                left += 1
                right -= 1
            
            # Check if the left half is sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target is in the left sorted half
                else:
                    left = mid + 1   # Target is in the right half
            
            # Otherwise, the right half must be sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Target is in the right sorted half
                else:
                    right = mid - 1  # Target is in the left half
                    
        return False
            

        