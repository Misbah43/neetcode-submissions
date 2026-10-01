class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
            
        # Step 1: Initialize candidates and counts
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
        # Phase 1: Find the top two candidates
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                # If the number matches neither candidate, decrement both counts
                count1 -= 1
                count2 -= 1
                
        # Phase 2: Verify the candidates
        result = []
        threshold = len(nums) // 3
        
        # Count actual occurrences in the array
        # Note: We use list.count() which iterates through the array again, 
        # making it a second O(n) pass, keeping total time O(n).
        if nums.count(candidate1) > threshold:
            result.append(candidate1)
            
        # Ensure candidate2 is not None and distinct, then verify
        if candidate2 != candidate1 and nums.count(candidate2) > threshold:
            result.append(candidate2)
            
        return result
        