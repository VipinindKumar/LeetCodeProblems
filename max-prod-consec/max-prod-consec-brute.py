def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return float("-inf")
        
        maxp = float("-inf")
        for i in range(n):
            for j in range(i, n):
                prod = 1
                for elm in nums[i:j+1]:
                    prod *= elm
                
                maxp = max(maxp, prod)
                
        return maxp
