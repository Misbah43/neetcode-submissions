class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
     
        # If the array is empty, there are 0 unique elements
        if not nums:
            return 0
            
        # The first element is always unique, so we start inserting at index 1
        insert_index = 1
        
        # Start scanning from the second element (index 1)
        for i in range(1, len(nums)):
            # If the current element is different from the previous one, it's a new unique number
            if nums[i] != nums[i - 1]:
                nums[insert_index] = nums[i]
                insert_index += 1
                
        # insert_index now represents the number of unique elements (k)
        return insert_index
       
    

        