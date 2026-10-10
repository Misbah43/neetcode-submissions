class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return " "
        count_t=Counter(t)
        window={}
        have,need=0,len(count_t)
        res_len=float('inf')
        res=[-1,-1]
        left=0
        for right, char in enumerate(s):
            window[char]=window.get(char,0)+1
            if char in count_t and window[char]==count_t[char]:
                have+=1
            while have==need:
                if(right-left+1)<res_len:
                    res=[left,right]
                    res_len=right-left+1
                window[s[left]]-=1
                if s[left]in count_t and window[s[left]]<count_t[s[left]]:
                    have-=1
                left+=1
        l,r=res
        return s[l:r+1] if res_len!=float('inf') else ""

            