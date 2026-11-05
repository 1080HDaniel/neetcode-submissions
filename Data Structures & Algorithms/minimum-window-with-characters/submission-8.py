class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # creates the thing
        key = {}
        for c in t:
            key[c] = key.get(c, 0) + 1
        
        john = {}
        i, j = 0, 0
        minans = ""
        have, need = 0, len(key)
        if len(t) > len(s):
            return ""
        
        for j in range(len(s)):
            g = s[j]
            john[g] = john.get(g, 0) + 1
            if g in key and john[g] == key[g]:
                have += 1 

            while have == need:
                if minans == "" or j - i + 1 < len(minans):
                    minans = s[i:j + 1]
                john[s[i]] -= 1
                if s[i] in key and john[s[i]] < key[s[i]]:
                    have -= 1
                i += 1
            j += 1
        return minans



