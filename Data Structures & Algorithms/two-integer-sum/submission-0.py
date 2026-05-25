class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx in range(len(nums)):
            if target - nums[idx] not in hashmap.keys():
                hashmap[nums[idx]] = idx
                continue
            else:
                return [hashmap[target - nums[idx]], idx]
                
