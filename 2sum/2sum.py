def twoSum(self, nums: List[int], target: int) -> List[int]:
    # returns index of two integers in nums that add to target
    # create a hash map of nums, for faster lookup
    numsHash = {nums[i]: i for i in range(len(nums))}
    
    for i, firstInt in enumerate(nums):
        lkup = target - firstInt
        
        if lkup in numsHash and i != numsHash[lkup]:
            return [i, numsHash[lkup]]
    
    return "not working"