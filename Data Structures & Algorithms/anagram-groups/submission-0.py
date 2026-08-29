from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for s in strs:
            count = [0] * 26          # frequency of each letter a-z
            for char in s:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)        # tuple so it's hashable (can be a dict key)
            groups[key].append(s)
        
        return list(groups.values())