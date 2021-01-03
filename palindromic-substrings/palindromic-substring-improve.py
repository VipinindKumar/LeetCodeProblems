def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            count += self.ispal(s, i, i)
            count += self.ispal(s, i, i+1)
        
        return count
    
    def ispal(self, s, i, j):
        n = len(s)
        count = 0
        while(i >= 0 and j < n and s[i] == s[j]):
            count += 1
            i -= 1
            j += 1
        return count
