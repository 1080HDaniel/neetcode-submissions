class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j = 0, 0
        john = {}
        maxlen = 0
        maxfreq = 0
        for j in range(len(s)):
            john[s[j]] = john.get(s[j], 0) + 1
            maxfreq = max(maxfreq, john[s[j]])
            while j - i + 1 - maxfreq > k:
                john[s[i]] -= 1
                i += 1
            maxlen = max(maxlen, j - i + 1)
        return maxlen
                

