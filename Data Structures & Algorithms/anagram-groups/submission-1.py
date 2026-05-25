class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # establish a character-idx mapping
        mapping = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7,
            "i": 8,
            "j": 9,
            "k": 10,
            "l": 11,
            "m": 12,
            "n": 13,
            "o": 14,
            "p": 15,
            "q": 16,
            "r": 17,
            "s": 18,
            "t": 19,
            "u": 20,
            "v": 21,
            "w": 22,
            "x": 23,
            "y": 24,
            "z": 25
        }
        
        # key is a list of size 26 where idx is the frequency of 
        # character in the alphabet (idx + 1)-th letter in the
        # alphabet in the word we're currently looking at
        result = []
        seen_freq = {}
        for str_ in strs:
            str_freq = [0] * 26
            for char in str_:
                str_freq[mapping[char]] += 1
            if str(str_freq) not in str(seen_freq.keys()):
                seen_freq[str(str_freq)] = [str_]
            else:
                seen_freq[str(str_freq)].append(str_)
        return list(seen_freq.values())
             
