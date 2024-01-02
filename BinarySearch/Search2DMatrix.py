class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we know that each row is non-decreasing order ... so elements increase or constnat
        # also first int of each row is > last int of row-1
        left = 0 
        right = len(matrix)-1

        while left <= right:
            mid = (left+right)//2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                l_sub = 0
                r_sub = len(matrix[mid])-1

                if target in matrix[mid]:
                        while l_sub <= r_sub:
                            # print('hi')
                            mid_sub = (l_sub+r_sub)//2
                            if matrix[mid][mid_sub] == target:
                                # print('1')
                                return True
                            elif matrix[mid][mid_sub] > target:
                                r_sub = mid_sub-1
                            elif matrix[mid][mid_sub] < target:
                                l_sub = mid_sub+1
                else:
                    return False
                        
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False