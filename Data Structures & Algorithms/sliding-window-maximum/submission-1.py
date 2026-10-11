class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # left=0
        # l=len(nums)-k+1
        # res=[]
        # while left<l:
        #     arr=nums[left:left+k]
        #     res.append(max(arr))
        #     left+=1
        # return res
        res=[]
        q=deque()#stores indices
        for right in range(len(nums)):
            while q and nums[q[-1]]<nums[right]:
                q.pop()
            q.append(right)
            if q[0]<=right-k:
                q.popleft()
            if right>=k-1:
                res.append(nums[q[0]])
        return res


        