class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                difference_temp = temp - stack[-1][1]
                answer[stack[-1][0]] = index - stack[-1][0]
                stack.pop()

            stack.append([index, temp])
        
        return answer 