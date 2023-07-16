class Solution:
   def setZeroes(self, matrix):
       
    m, n = len(matrix), len(matrix[0])
    rows, cols = set(), set()

    # Iterate over the matrix to find all rows and columns that contain a zero
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    # Set the elements in these rows and columns to zero
    for i in range(m):
        for j in range(n):
            if i in rows or j in cols:
                matrix[i][j] = 0

    return matrix
