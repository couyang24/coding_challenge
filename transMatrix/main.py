A = [[1,2,3],[4,5,6]]

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:

        row = len(A)
        col = len(A[0])

        #print(row)
        #print(col)

        matrix = [[0 for x in range(row)] for y in range(col)]
        #print(matrix)


        for tcol, row in enumerate(A):
            for trow, item in enumerate(row):
                matrix[trow][tcol] = item

        #print(matrix)
        return matrix