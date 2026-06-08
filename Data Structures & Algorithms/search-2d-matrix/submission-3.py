class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrixl, matrixr = 0, len(matrix) - 1
        index = -1
        while matrixl <= matrixr:
            middle = (matrixl + matrixr)//2
            if target <= matrix[middle][-1] and target >= matrix[middle][0]:
                print("1")
                index = middle
                break
            elif target < matrix[middle][0]:
                print("2")
                matrixr = middle - 1
                print(matrixl, matrixr)
            else:
                print("3")
                matrixl = middle + 1
        # answer = False
        print(index)
        if not index == -1:
            l, r = 0, len(matrix[index]) - 1
            while l <= r:
                mid = (l + r)//2
                if target == matrix[index][mid]:
                    return True
                elif target > matrix[index][mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
            