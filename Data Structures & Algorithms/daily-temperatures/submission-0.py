class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        
        # The stack will store the INDICES of the temperatures, not the temperatures themselves
        stack = [] 
        
        for i, t in enumerate(temperatures):
            # While the stack has people waiting, AND today's temperature is warmer
            # than the temperature of the day at the top of the stack
            while stack and t > temperatures[stack[-1]]:
                # Pop the index of the colder day
                prev_i = stack.pop()
                # The number of days waited is today's index minus the popped index
                res[prev_i] = i - prev_i
                
            # Add today's index to the waiting room
            stack.append(i)
            
        return res
        