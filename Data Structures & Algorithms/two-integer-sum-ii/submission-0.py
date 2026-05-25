class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        diff = numbers[1] - numbers[0]
        idx1 = 0
        idx2 = len(numbers) - 1

        if diff == 0:
            return [idx1 + 1, idx2 + 1]

        while idx1 < idx2:
            if target - numbers[idx1] - numbers[idx2] == 0:
                return [idx1 + 1, idx2 + 1]
            elif target - numbers[idx1] - numbers[idx2] < 0:
                # decrement idx2 to lower to negative diff
                idx2 -= 1
            else:
                # increment idx1 to increase the diff
                idx1 += 1
            
