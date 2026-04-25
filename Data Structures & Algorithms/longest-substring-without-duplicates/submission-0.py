class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hmap = {}
        window = 0
        res = 0

        for i in range(len(s)):
            if s[i] in hmap:
                window = max(hmap[s[i]] + 1, window)
            
            hmap[s[i]] = i
            res = max(res, i - window + 1)
        
        return res