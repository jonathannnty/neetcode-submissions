class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq = []
        nums = sorted(nums)
        
        # brute force solution
        for idx in range(len(nums)):
            curr_num = [nums[idx]]
            for idx2 in range(idx,len(nums)):
                if curr_num[len(curr_num) - 1] == nums[idx2] - 1:
                    curr_num.append(nums[idx2])
            print(curr_num)
            if longest_seq == None:
                longest_seq = curr_num
            if len(longest_seq) < len(curr_num):
                longest_seq = curr_num
        return len(longest_seq)