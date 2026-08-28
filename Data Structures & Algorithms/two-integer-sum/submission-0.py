class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i ,num in enumerate(nums):
            for j,num in enumerate(nums):
              if(i!=j):
               if (nums[i]+nums[j]==target ):
                return [i,j];
            