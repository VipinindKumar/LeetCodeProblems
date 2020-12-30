  GNU nano 4.9.2         max-consecutives1/max-consecutive.py         Modified













def longestOnes(self, A: List[int], K: int) -> int:
	n = len(A)
	if n == 0:
	    return 0

	left, right = 0, 0
	numzeros = 0
	longsub = 0

	while right < n:
	    # if new addition to sub is 0, then inc. the count of 0s
	    if A[right] == 0:
	        numzeros += 1
	    
	    # if numzeros exceed limit of K
	    # keep removing left most element to bring numzeros to K
	    while numzeros > K:
	        # if left element is 0 dec. the count of 0s
	        if A[left] == 0:
	            numzeros -= 1
	        left += 1
	    
	    if (right - left + 1) > longsub:
	        longsub = right - left + 1
	    
	    right += 1

	return longsub
