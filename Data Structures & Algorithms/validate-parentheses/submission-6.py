class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        for c in s:
            if c in '({[': #if opening bracket
                stack.append(c)
            elif len(stack) == 0 or stack.pop() != pairs[c]:
                return False
        return not stack