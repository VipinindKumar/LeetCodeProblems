def threeSum(self, nums: List[int]) -> List[List[int]]:
    # returns empty array if not enough elements
    n = len(nums)
    if n < 3:
        return []
    
    # sort the nums list
    nums.sort()
    
    result = []
    for i in range(n - 2):
        # to catch duplicates
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        l, r = i + 1, n - 1
        
        while l < r:
            sm = nums[i] + nums[l] + nums[r]
            
            if sm < 0:
                l += 1
            elif sm > 0:
                r -= 1
            else:
                result.append([nums[i], nums[l], nums[r]])
                
                while l < n-1 and nums[l] == nums[l+1]:
                    l += 1
                while r > 1 and nums[r] == nums[r-1]:
                    r -= 1
                
                l += 1
                r -= 1
        
    return result