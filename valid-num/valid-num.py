def isNumber(self, s: str) -> bool:
        s = s.strip()
        
        pattern = "^[-+]?((\d+(\.\d*)?)|\.\d+)(e[-+]?\d+)?$"
        if re.match(pattern, s):
            return True
        else:
            return False
