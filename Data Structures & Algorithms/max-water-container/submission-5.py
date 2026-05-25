class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        area = (right - left) * min(heights[right], heights[left])

        while left < right:
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
            area = max(area, (right - left) * min(heights[right], heights[left]))
        return area
            
            