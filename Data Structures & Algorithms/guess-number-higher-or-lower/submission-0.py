# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # n, int: its mean to denote the range of possible values
        # this person could've picked
        # we can call guess to help us deduce where this secret number is in our range
        # binary search
        left = 1
        right = n

        while left <= right:
            middle = (left + right)//2
            num = guess(middle)

            if num == 0:
                return middle
            elif num == -1:
                right = middle - 1
            else:
                left = middle + 1