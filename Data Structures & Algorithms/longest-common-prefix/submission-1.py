class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        min_ = len(min(strs, key=len))

        for c_idx in range(min_):
            c = strs[0][c_idx]
            for str_ in strs:
                if str_[c_idx] != c:
                    return output
            output = output + c
        return output