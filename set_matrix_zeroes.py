class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=[]
        n=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    m.append(i)
                    n.append(j)

        for i in m:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

        for i in range(len(matrix)):
            for j in n:
                matrix[i][j] = 0

        return matrix


#2nd Method
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = [0] * len(matrix)
        n = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    m[i] = 1 
                    n[j] = 1
        for i in range(len(m)):
            for j in range(len(n)):
                if m[i] or n[j]:
                    matrix[i][j] = 0
        return matrix


















        
