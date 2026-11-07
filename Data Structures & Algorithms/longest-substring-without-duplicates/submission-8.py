class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        start = 0
        max_length = 0
        length = 0
        for i, c in enumerate(s):
            if c in d:
                start = max(d[c] + 1, start)
                d[c] = i
            else: 
                d[c] = i
            #print(i, start, d, c)
            length = i - start + 1
            if length > max_length:
                max_length = length

        return max_length
