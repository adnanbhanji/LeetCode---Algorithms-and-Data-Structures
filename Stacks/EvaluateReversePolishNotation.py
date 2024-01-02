class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in "+-*/":
                new_stack = stack[-2:]
                if i == "+":
                    stack.pop()
                    stack.pop()
                    stack.append(int(new_stack[0]) + int(new_stack[1]))
                elif i == "*":
                    stack.pop()
                    stack.pop()
                    stack.append(int(new_stack[0]) * int(new_stack[1]))
                if i == "/":
                    stack.pop()
                    stack.pop()
                    stack.append(int(new_stack[0]) / int(new_stack[1]))
                if i == "-":
                    stack.pop()
                    stack.pop()
                    stack.append(int(new_stack[0]) - int(new_stack[1]))
            else:
                stack.append(i)
                
        return int(stack[0])