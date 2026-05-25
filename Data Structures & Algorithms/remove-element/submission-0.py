class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, 0

        while right < len(nums):
            print(f"left: {left}, right: {right}")
            if nums[right] == val:
                right += 1
            else:
                nums[left] = nums[right]
                left += 1
                right += 1
            print(f"nums: {nums}")
        return left