class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counter = 0
        for i in range(len(flowerbed)):
            if i == 0: 
                if len(flowerbed) == 1:
                    if flowerbed[i] == 0:
                        flowerbed[i] = 1
                        counter += 1
                else:
                    if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        counter += 1
            elif i == (len(flowerbed) - 1):
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    counter += 1
            else:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1]==0:
                    flowerbed[i] = 1
                    counter += 1
        return True if counter >= n else False
            