def threeSum(self, nums: List[int]) -> List[List[int]]:
        # returns empty array if not enough elements
        n = len(nums)
        if n < 3:
            return []
        
        # sort the nums list
        nums.sort()
        
        # set of nums for faster lookup
        numSet = {integer: i for i, integer in enumerate(nums)}
        
        result = []
        for i in range(n):
            for j in range(i+1,n):
                int1 = nums[i]
                int2 = nums[j]
                
                # look for 3sum0 and use index to reject duplicates
                int3 = -(int1 + int2)
                if int3 in numSet:
                    index = numSet[int3]
                    if i < index and j < index and [int1,int2,int3] not in result:
                        result.append([int1, int2, int3])
                    
        return result
