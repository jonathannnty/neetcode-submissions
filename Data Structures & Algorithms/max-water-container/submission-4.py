class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        max_ = (right - left) * min(heights[left], heights[right])

        # greedy, choose which pointer to move based on which one
        # is the minimum height
        while left < right:
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
            max_ = max((right - left) * min(heights[left], heights[right]), max_)
            print(max_)
        return max_

