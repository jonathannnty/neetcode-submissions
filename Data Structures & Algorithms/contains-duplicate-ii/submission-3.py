class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # input: list of integers, k (target)
        # output True or False (if if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k, otherwise return false.)

        if len(nums) < 2 or len(nums) > 2 and k == 0:
            return False

        # Sliding window approach
        # len(nums) > 1
        left, right = 0, 1

        while right < len(nums):
            if left == right:
                right += 1
            elif abs(left - right) > k:
                left += 1
                right = left
            elif nums[left] == nums[right]:
                return True
            right += 1 
        return False
