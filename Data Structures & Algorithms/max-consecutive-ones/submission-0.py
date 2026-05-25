class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # inputs = nums, list of integers
        # output = integer
        # greatest number of consecutive 1 we've encountered

        # iterate through nums, have a tracker to count the number of consec. 1's we've encountered
        # if ever we encounter a 0, this tracker is reset
        # additionally, we would want another variable to keep track of the greatest number
        # this tracker has ever been
        # each time this tracker is incremented (meaning we encountered a 1)
        # we want to see if the tracker is greater than this variable kept of the greatest number
        # if so, we reassigned this variable to be tracker
        tracker = 0
        max_ = 0

        for num in nums:
            if num == 1:
                tracker += 1
                max_ = max(tracker, max_)
            else:
                tracker = 0
        
        return max_