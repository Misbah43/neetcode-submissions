class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
       
        for aster in asteroids:
            while stack and stack[-1]>0 and aster <0:
                diff=aster+stack[-1]
                if diff <0:
                    stack.pop()
                elif diff>0:
                    break
                else:
                    stack.pop()
                    break
            else:
                stack.append(aster)
        return stack
            



        