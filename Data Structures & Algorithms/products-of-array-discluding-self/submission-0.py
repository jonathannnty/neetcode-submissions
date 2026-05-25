class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = nums[0]
        suffix = 1
        
        for num in nums[1:]:
            suffix = suffix * num
        
        # prefix = nums[0] = 1
        # suffix = product of nums[1:] = 48 
        
        nums[0] = suffix

        # output: [48, x , x, x]

        for idx in range(1, len(nums)):
            print(f"old suffix: {suffix}")
            if nums[idx] != 0:
                suffix = suffix//nums[idx]
            else:
                suffix = 1
                for num in nums[idx + 1:]:
                    suffix = suffix * num
            print(f"new suffix: {suffix}")

            temp = nums[idx]
            
            nums[idx] = suffix * prefix
            print(f"multiplying suffix {suffix} with prefix {prefix}, resulting in nums[{idx}] = {suffix * prefix}")
            
            print(f"multiplying prefix {prefix} with nums[{idx - 1}] = {nums[idx - 1]}, resulting in prefix = {prefix * nums[idx - 1]}")
            prefix = prefix * temp
            print(f"new prefix: {prefix}")

            print(f"nums (output) = {nums}")
        
        return nums
        # Output: [48,24,12,8]
