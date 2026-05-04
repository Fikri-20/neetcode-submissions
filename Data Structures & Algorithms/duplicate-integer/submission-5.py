class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_pos = [0] * 20000
        freq_neg = [0] * 20000
        for i in nums:
            if(i >= 0): 
                freq_pos[i] += 1 
            else: 
                freq_neg[-i] += 1
        for i in nums: 
            if(i >= 0): 
                if(freq_pos[i] > 1):
                    return True
            else: 
                if(freq_neg[-i] > 1): 
                    return True
        return False
                 