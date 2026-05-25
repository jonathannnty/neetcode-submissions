class Solution:
    def validPalindrome(self, s: str, deletion=False) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                if deletion:
                    return False
                del_l = self.validPalindrome(s[left + 1:right + 1], True)
                del_r = self.validPalindrome(s[left:right], True)
                if del_l or del_r:
                    deletion
                    return True
                else:
                    return False
            else:
                left += 1
                right -= 1
        return True