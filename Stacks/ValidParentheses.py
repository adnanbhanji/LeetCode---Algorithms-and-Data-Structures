class Solution:
    def isValid(self, s: str) -> bool:
        possibilities = {
            "{": "}",
            "(": ")",
            "[": "]",
        }

        stack = []
        
        if len(s) % 2 != 0:
            return False
        
        for i in s:
            if i in possibilities.keys():
                stack.append(possibilities[i])
            else:
                if not stack or i != stack[-1]:
                    return False
                stack.pop()
        
        return len(stack) == 0
