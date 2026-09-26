class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
            
        # Divide the array in half
        mid = len(nums) // 2
        
        # Recursively sort the left and right halves
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])
        
        # Merge the two sorted halves together
        return self.merge(left_half, right_half)
        
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        sorted_arr = []
        i, j = 0, 0
        
        # Two-pointer approach to merge two sorted arrays
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1
                
        # If there are leftovers in either array, append them to the end
        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])
        
        return sorted_arr

        

        