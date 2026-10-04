class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        empty={}
        res=0
        left=0
        for i , char in enumerate(s):
            if char in empty and empty[char]>=left:
                left=empty[char]+1
            empty[char]=i
            value=i-left+1
            res=max(res,value)
            
        return res
        