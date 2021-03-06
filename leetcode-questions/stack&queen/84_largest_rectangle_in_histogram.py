class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        res = 0
        
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
                res = max(res, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        
        while stack[-1] != -1:
            res = max(res, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        
        return res