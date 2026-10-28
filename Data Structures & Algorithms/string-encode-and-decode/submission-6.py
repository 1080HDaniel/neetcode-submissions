class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
            encoded_string = encoded_string + str(len(i)) +"#" +  i
        return encoded_string;

    def decode(self, s: str) -> List[str]:
        decoded_strs, i = [], 0
        while i < len(s):
            if s[i] == "#":
                length = int(s[:i])
                decoded_strs.append(s[i+1:i+1+length])
                s = s[i + length + 1:]
                i = 0
            i += 1
        return decoded_strs;
