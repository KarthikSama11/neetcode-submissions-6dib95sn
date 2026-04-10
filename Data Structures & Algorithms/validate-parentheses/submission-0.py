class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braces = {'}':'{', ']':'[', ')':'('}


        for b in s:
            if b in ('(','{','['):
                stack.append(b)
            else:
                if len(stack) <= 0 or stack[-1] != braces[b]:
                    return False
                else :
                    stack.pop()
        return True if len(stack) == 0 else False
                
