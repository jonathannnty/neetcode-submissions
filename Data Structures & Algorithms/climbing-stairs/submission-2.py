class Solution:
    def climbStairs(self, n: int) -> int:
        # input: integer
        # output: integer, the number of different ways to reach that input integer
        # through a series of adding either 1's or 2's

        # dynamic programming
        # create a list of length n, where the i-th element is the correctly computed way
        # of reaching i steps of a staircase through a combination of 1 or 2 steps at a time
        # we can leverage the previous computed ways to reach i-th elements all the way to the (n-1)th
        # element in this list

        list_ = [0] * n

        # base case
        list_[0] = 1

        if len(list_) == 1:
            return list_[0]
        
        list_[1] = 2

        for idx in range(2, len(list_)):
            list_[idx] = list_[idx - 1] + list_[idx - 2]
        
        return list_[len(list_) - 1]