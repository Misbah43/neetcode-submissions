class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i , num in enumerate(nums):
            if num >0:
                break
            if i>0 and num==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k :
                current_sum=nums[i]+nums[j]+nums[k]
                if current_sum>0:
                    k-=1
                elif current_sum<0:
                    j+=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                      j+=1
                
        return res
            
     
            
        