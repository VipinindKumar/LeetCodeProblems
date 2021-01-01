def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)
        if n % 2 != 0:
            return False
        
        for c in s:
            # if c is open parentheses
            if c in ['(', '[', '{']:
                stack.append(c)
            elif stack:
                openp = stack.pop()
                if c == ')' and openp == '(':
                    continue
                elif c == ']' and openp == '[':
                    continue
                elif c == '}' and openp == '{':
                    continue
                else:
                    return False
            else:
                return False
        
        if not stack:
            return True
        else:
            return False
