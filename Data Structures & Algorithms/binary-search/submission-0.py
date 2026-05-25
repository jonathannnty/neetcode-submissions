class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # input is a sorted list of ints, target is an int
        # output is the index for which target can be found in this
        # sorted list of ints, if not found then we return -1
        
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (right + left)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1