class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        tot_len = 0
        mn_len = 205
        for wd in strs:
            tot_len = max(tot_len, len(wd))
            mn_len = min(mn_len, len(wd))
        res = ""
        for i in range(tot_len):
            match = True
            match_chr = ''
            if(i >= mn_len): 
                match = False
                break
            else: 
                match_chr = strs[0][i]
            for wd in strs: 
                if(wd[i] != match_chr): 
                    match = False
                    break 
            if(match): 
                res += match_chr 
            else: 
                break 
        return res    

        