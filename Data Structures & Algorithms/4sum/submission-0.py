class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n - 3):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Early pruning: if smallest possible sum is too large, break
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            # Early skipping: if largest possible sum is too small, continue
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
                continue
                
            for j in range(i + 1, n - 2):
                # Skip duplicates for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # Early pruning for second loop
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target:
                    continue
                    
                # Two-pointer approach for the remaining two numbers
                l, r = j + 1, n - 1
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    
                    if total == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        
                        l += 1
                        r -= 1
                        # Skip duplicates for the third number
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        # Skip duplicates for the fourth number
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1
                        
        return res