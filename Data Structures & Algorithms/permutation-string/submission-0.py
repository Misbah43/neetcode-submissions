class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        freq_s1=Counter(s1)
        window_size=len(s1)
        freq_s2=Counter()
        for i in range(len(s2)):
          freq_s2[s2[i]]+=1
          if i>=window_size:
            left=s2[i-window_size]
            freq_s2[left]-=1
            if freq_s2[left]==0:
                del freq_s2[left]
          if freq_s2==freq_s1:
            return True
        return False

        
   
        