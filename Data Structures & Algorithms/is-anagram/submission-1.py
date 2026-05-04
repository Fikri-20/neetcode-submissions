class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha_s = [0] * 26
        alpha_t = [0] * 26
        for i in s: 
            alpha_s[ord(i)-ord('a')] += 1
        for i in t: 
            alpha_t[ord(i)-ord('a')] += 1
        for i in range(len(alpha_s)): 
            if alpha_s[i] != alpha_t[i]: return False
        return True