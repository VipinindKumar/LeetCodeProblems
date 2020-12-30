def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        result = float("-inf")
        
        if n == 0:
            return result
        
        # max and min values upto the current index
        currmax, currmin = 1, 1
        
        for i in range(n):
            # if ith num is -ve, need to exchange current max, min
            # -ve will make currmin the max upto now
            if nums[i] < 0:
                temp = currmax
                currmax = currmin
                currmin = temp
            
            currmax = max(nums[i], nums[i] * currmax)
            currmin = min(nums[i], nums[i] * currmin)
            
            result = max(result, currmax)
        
        return result
