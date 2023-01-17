class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        total = 0
        all_mods = {0:-1} # hash table containing many mod values of the total, paired with current index
        
        for i, n in enumerate(nums):
            total += n
            
            if total % k in all_mods:
                if i - all_mods[total % k] >= 2:
                    return True
            else:
                all_mods[total % k] = i
        
        return False