class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        possible_values = self.map[key] #arr of all possible vals
        left = 0
        right = len(possible_values)-1
        final_res = ""

        while left <= right:
            mid = (left+right)//2
            if possible_values[mid][1] <= timestamp:
                final_res = possible_values[mid][0]
                left = mid+1
            else:
                right = mid-1

        
        return final_res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)