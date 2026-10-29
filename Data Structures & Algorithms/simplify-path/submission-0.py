class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        # Split the path by '/' to process each component
        components = path.split("/")
        
        for comp in components:
            if comp == "..":
                if stack:
                    stack.pop()
            elif comp and comp != ".":
                stack.append(comp)
                
        # Reconstruct the canonical path
        return "/" + "/".join(stack)