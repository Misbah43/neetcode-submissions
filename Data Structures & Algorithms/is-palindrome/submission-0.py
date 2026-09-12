class Solution:
    def isPalindrome(self, s: str) -> bool:
        my_list=[char.lower() for char in s if char.isalnum()]
        for i in range(len(my_list)//2):
            j=len(my_list)-1-i
            if my_list[i]!=my_list[j]:
                return False
        return True
            
        