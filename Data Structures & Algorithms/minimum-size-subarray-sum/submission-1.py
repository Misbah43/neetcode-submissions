class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        res=float('inf')
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            while sum>=target:
                window=i-left+1
                res=min(res,window)
                sum-=nums[left]
                left+=1
        return res if res!=float('inf') else 0

        
        