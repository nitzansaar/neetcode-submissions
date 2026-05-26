class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if self.isOpenBracket(c):
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif (c == ')' and stack.pop() != '(' or \
                    c == ']' and stack.pop() != '[' or \
                    c == '}' and stack.pop() != '{'):
                return False
        return len(stack) == 0

    def isOpenBracket(self, char):
        return char == '[' or char == '{' or char == '('