class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    #    def product_except(i):
    #     p=1
    #     for j,num in enumerate(nums):
    #         if j!=i:
    #             p*=num
    #     return p
    #    return list(map(product_except,range(len(nums))))
        n=len(nums)
        result=[1]*n

        prefix=1
        for i in range(n):
          result[i]=prefix
          prefix*=nums[i]
        
        suffix=1
        for i in range (n-1,-1,-1):
          result[i]*=suffix
          suffix*=nums[i]
        return result





    
    

          
