class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}
        if len(s) != len(t):
            return False
        for char_s, char_t in zip(s, t):
            if char_s not in count_s: 
                count_s[char_s] = 1
            else:
                count_s[char_s] += 1
            if char_t not in count_t: 
                count_t[char_t] = 1
            else:
                count_t[char_t] += 1
        for key in count_s.keys():
            if key not in count_t.keys():
                return False
            if count_t[key] != count_s[key]:
                return False
        return True