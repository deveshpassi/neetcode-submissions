class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        left = 0
        maxFreq = 0
        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)
            maxFreq = max(maxFreq, count[s[i]])

            while (i - left + 1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, i - left + 1)

        return res 
            