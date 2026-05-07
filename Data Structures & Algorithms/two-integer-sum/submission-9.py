class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        st = 0
        end = len(nums) - 1
        while end > st:
            sum = sorted_nums[end] + sorted_nums[st]
            if(sum == target): 
                break
            elif (sum > target): 
                end -= 1
            else: 
                st += 1
        print(st, end)
    
        mn = min(sorted_nums[st], sorted_nums[end])
        mx = max(sorted_nums[st], sorted_nums[end])
        i = nums.index(mn)
        if mn == mx: 
            j = nums.index(mx, i+1)
        else: 
            j = nums.index(mx)
            
        return [min(i,j),max(i,j)]
        