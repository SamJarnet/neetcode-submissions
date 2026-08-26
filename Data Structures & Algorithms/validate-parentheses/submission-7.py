class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        valid = True
        stack = []
        if s.count('(') != s.count(')') or s.count('[') != s.count(']') or s.count('{') != s.count('}'):
            return False
        for i in range(0, len(s)):
            if s[i] == '{' or s[i] == '[' or s[i] == '(':
                stack.append(s[i])
            else:
                if stack == []:
                    return False
                parenth = stack.pop()
                if parenth == '{':
                    if s[i] != '}':
                        valid = False
                elif parenth == '(':
                    if s[i] != ')':
                        valid = False
                elif parenth == '[':
                    if s[i] != ']':
                        valid = False
        return valid
                
