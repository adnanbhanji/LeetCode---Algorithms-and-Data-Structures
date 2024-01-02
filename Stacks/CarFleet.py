class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        slow_car = 0
        answer = 0

        for position, speed in sorted(zip(position, speed), reverse=True):
            # time = dis / speed
            eta = (target-position) / speed

            if eta > slow_car:
                answer += 1
                slow_car = eta
        
        return answer