class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # input being two words (word1 str, word2 str)
        # we want to output a string st it is the combination of the two but alternating
        # two pointers (0, 0 to the be index values of string 1 and string 2), create a result string
        # while-loop (when we do we stop? we reach the end of either two of our words)
        word1_len = len(word1)
        word2_len = len(word2)
        p = 0
        output = ""

        while p < word1_len and p < word2_len:
            output = output + word1[p] + word2[p]
            p += 1

        if word1_len == word2_len:
            return output
        elif word1_len < word2_len:
            return output + word2[p:]
        else:
            return output + word1[p:]
