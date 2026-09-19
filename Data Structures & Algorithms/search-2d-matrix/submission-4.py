class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0: return -1
        start = 0
        n = len(matrix)
        m = len(matrix[0])
        end = n*m - 1
        while start <= end:
            mid = (end + start) // 2
            row = mid // m
            column = mid % m
            print(start, end, mid, target, row, column)
            print(matrix[row][column])
            if matrix[row][column] == target: 
                return True
            elif matrix[row][column] > target:
                end = mid - 1
            elif matrix[row][column] < target:
                start = mid + 1
        return False