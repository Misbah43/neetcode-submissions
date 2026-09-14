class Solution:
    def validPalindrome(self, s: str) -> bool:
        # freq = Counter(s)
        # unfiltered=[char for char in s if freq[char]<=1]
        # if len(unfiltered)<=1 :
        #   filtered = [char for char in s if freq[char] > 1]
        #   new_list=[char.lower() for char in filtered if char.isalnum()]
        #   for i in range(len(new_list)//2):
        #     j=len(new_list)-i-1
        #     if new_list[i]!=new_list[j]:
        #         return False
        # else :
        #     return False
        # return True
        left =0
        right=len(s)-1
        while left<right:
         if s[left]!=s[right]:
            skip_left=s[left+1:right+1]
            skip_right=s[left:right]
            return skip_left==skip_left[::-1] or skip_right==skip_right[::-1]
         left+=1
         right-=1
        return True
        

            


        