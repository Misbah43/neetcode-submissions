class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}  # Tracks the frequency of characters in our window
        res = 0
        max_freq = 0  # Tracks the frequency of the single most common character in the window
        
        for right in range(len(s)):
            # Add the current character to our frequency map
            char = s[right]
            count[char] = count.get(char, 0) + 1
            
            # Keep track of the highest frequency seen so far in this window
            max_freq = max(max_freq, count[char])
            
            # Check if our window is invalid: 
            # (Window Length - Most Frequent Character Count) > k
            # If it's invalid, shrink the window from the left
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
                
            # Update our maximum window size result
            res = max(res, right - left + 1)
            
        return res


        