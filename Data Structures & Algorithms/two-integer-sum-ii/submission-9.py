class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while left<right:
            current_sum=numbers[left]+numbers[right]
            if current_sum==target:
                return [left+1,right+1]
            elif current_sum > target:
                right-=1
            else :
                left+=1


        # for i , num in enumerate(numbers):
        #     if target-numbers[i] in numbers:
        #         j=numbers.index(target-numbers[i])
        #         while numbers[i]!=numbers[j] and numbers[i]<numbers[j]:
        #          final=list([numbers[i],target-numbers[i]])
        #          return final
        # return 0

            # for j ,num in enumerate(numbers):
            #     while numbers[i]!=numbers[j]:
            #         if  numbers[i]+numbers[j] ==target:
            #             return [numbers[i],numbers[j]]
        