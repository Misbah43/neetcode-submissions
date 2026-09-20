class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing brackets to their corresponding opening brackets
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty, else use a dummy value
                top_element = stack.pop() if stack else "#"
                
                # If the popped bracket doesn't match the expected opening bracket, it's invalid
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty at the end, all brackets were properly closed
        return not stack
                
        