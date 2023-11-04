class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counter_flowers = 0
        len_flowerbed = len(flowerbed)

        if len_flowerbed < 2:
            if flowerbed[0] == 0 and n < 2:
                return True

        for i in range(len_flowerbed):
            if i == 0 or i == len_flowerbed-1:
                if i == 0 and flowerbed[i] == 0 and flowerbed[i+1]==0:
                    counter_flowers+=1
                    flowerbed[i] = 1
                if i==len_flowerbed-1 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    counter_flowers += 1
                    flowerbed[i] = 1
            else:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    counter_flowers += 1

        return True if counter_flowers >= n else False