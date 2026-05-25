class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq = []
        for num in nums:
            if num not in uniq:
                uniq += [num]
            else:
                return True
        return False