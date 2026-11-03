class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, john = 0, 1, set()
        maxlen = 1 if s else 0
        if len(s) == 1:
            return 1
        while j < len(s):
            john.add(s[i])
            while s[j] in john:
                john.remove(s[i])
                i += 1
            john.add(s[j])
            maxlen = max(maxlen, j - i + 1)
            j += 1
        return maxlen