palset = set()
def ispal(self, subs: str) -> bool:
    '''Return True if sting is palindrome,
        False otherwise'''
    if subs in self.palset:
        return True
    
    ns = len(subs)
    if ns == 0:
        return True
    elif ns == 1:
        return True

    if subs[0] == subs[-1]:
        if self.ispal(subs[1:-1]):
            self.palset.add(subs)
            return True
    
    return False
    
def countSubstrings(self, s: str) -> int:
    n = len(s)
    count = 0
    
    for i in range(n):
        for j in range(i+1, n+1):
            subs = s[i:j]
            if self.ispal(subs):
                count += 1
    return count
