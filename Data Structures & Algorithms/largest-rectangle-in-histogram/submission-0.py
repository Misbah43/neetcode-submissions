class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # pairs: (index, height)

        for i, h in enumerate(heights):
            start = i
            # Pop elements from stack that are taller than current height h
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx  # Current height can extend backwards to idx
            
            stack.append((start, h))

        # Check remaining bars that extended to the end of the histogram
        n = len(heights)
        for idx, height in stack:
            max_area = max(max_area, height * (n - idx))

        return max_area
        