class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # method 1
        # len_s1 = len(s1)
        # len_s2 = len(s2)  
        # if len_s1 > len_s2:
        #     return False

        # sorted_permutation = sorted(s1)

        # anchor = 0
        # right = len_s1

        # while right <= len_s2:
        #     substr = s2[anchor:right]
        #     if sorted(substr) == sorted_permutation:
        #         # print(sorted(substr), sorted_permutation)
        #         return True

        #     anchor += 1           
        #     right += 1           
    
        # return False
        
        # method2
        store = {}
        len_s1 = len(s1)
        len_s2 = len(s2)  
        if len_s1 > len_s2:
            return False
        
        for i in s1:
            if i not in store:
                store[i] = 1
            else:
                store[i] += 1

        anchor = 0
        right = len_s1
        temp = {}

        while right <= len_s2:
            for i in range(anchor, right):
                if s2[i] not in temp:
                    temp[s2[i]] = 1
                else:
                    temp[s2[i]] += 1
            
            print(temp)
            if temp == store:
                return True
            
            temp = {}
            anchor += 1           
            right += 1           

        return False

