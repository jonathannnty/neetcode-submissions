class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # input List of integers called nums
        # output: index values in nums such that the values stored at these indices
        # are unique

        # output initialize an empty list
        output = []

        # sort the nums array, strive for a two-pointer solution
        # where we're iterating through nums at idx i, and the two pointers are assigned i + 1
        # len(nums) - 1 respectively
        # if we know that number at idx i + number at idx i + 1 and len(nums) - 1 == 0
        # we can add that to output
        # idx i + number at idx i + 1 and len(nums) - 1 > 0, move the left pointer to the right
        # otherwise, right pointer to the left
        # process repeats until there left and right meet

        nums = sorted(nums)
        print(f"nums: {nums}")

        for idx in range(len(nums)):
            left = idx + 1
            right = len(nums) - 1
            print(f"left: {left}, right: {right}, idx: {idx}, idx elem: {nums[idx]}")
            while left < right:
                print(f"left elem: {nums[left]}, right elem: {nums[right]}")
                if nums[idx] + nums[left] + nums[right] == 0 and [nums[idx], nums[left], nums[right]] not in output:
                    print(f"inserting {[nums[idx], nums[left], nums[right]]}")
                    output.append([nums[idx], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[idx] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return output
