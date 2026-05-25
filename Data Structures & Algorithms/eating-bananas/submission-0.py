class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        
        left = 1
        right = max_pile

        while left <= right:
            middle = (right + left)//2
            min_h = 0
            for pile in piles:
                min_h += math.ceil(pile/middle)
            if min_h <= h:
                right = middle - 1
            else:
                left = middle + 1
        return left

            