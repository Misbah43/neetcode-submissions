class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        else:
            for s, char in enumerate(strs[0]):
                for other in strs[1:]:
                    if s>=len(other) or other[s]!=char:
                      return strs[0][:s]
        return strs[0]


        