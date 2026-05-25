class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # is it guaranteed that this nums array input is ascending by 1 like in the example?
        # binary search but the question how we can do that if the array has shifted some
        # number of times?

        # input: list of numbers
        # output: its minimum

        # the element on the left is less than middle and if the right is less than both
        # middle and left, reassigned left = middle + 1
        # the element on the left is greater than middle and middle is less than right
        left = 0
        right = len(nums) - 1
        while left <= right:
            print(f"we're looking at {nums[left:right+1]}")
            middle = (left + right)//2
            if left == right:
                return nums[left]
            if nums[left] <= nums[middle] and nums[middle] < nums[right]:
                right = middle
            elif nums[left] >= nums[middle] and nums[middle] > nums[right]:
                left = middle + 1
            elif nums[middle] > nums[left] and nums[middle] < nums[right]:
                left = middle
            elif nums[middle] < nums[left] and nums[middle] < nums[right] and nums[left] < nums[right]:
                right = middle
            elif nums[middle] < nums[left] and nums[middle] < nums[right] and nums[left] > nums[right]:
                right = middle
            else:
                left = middle
        
        # [1,2,3] [3,1,2] [2,3,1]
        # [1,2,3] > left = 1, right = 3, middle = 2
        # left <= middle < right --> right = middle
        # left = middle = 1, right = 2 --> right = middle --> left == right > return nums[left]

        # [3,1,2] > left = 3, right = 2, middle = 1
        # left > middle > right --> left = middle
        # left = middle = 1, right = 2 --> right = middle --> left == right > return nums[left]

        # [2,3,1] > left = 2, right = 1, middle = 3
        # middle > left BUT middle < right --> left = middle + 1
        # left = 1, middle = 1, right = 1 --> left == right > returns nums[left]

                
        
