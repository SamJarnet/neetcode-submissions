class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        temp = []
        for i in range(0, len(matrix)):
            temp += matrix[i]
        return (target in set(temp))