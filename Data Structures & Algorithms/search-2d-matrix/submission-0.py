class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # matrix: Lists of Lists, where in the inner-lists, it contains ints
        # target: int

        # if target even exists in this matrix
        # m = the length of matrix
        # n = the length of one element in matrix
        # m * n = elements to search for
        # first element in the matrix[0][0]
        # last element in the matrix[m - 1][n - 1]

        # middle element in the matrix[(0 + m)//2][(0 + n)//2]
        m_rows = len(matrix)
        n_cols = len(matrix[0])
        left, right = 0, m_rows * n_cols - 1

        while left <= right:
            print(f"left: {left}, right: {right}")
            mid = (left + right)//2
            print(f"middle: {mid}")
            mid_r, mid_c = mid//n_cols, mid % n_cols
            print(f"row: {mid_r}, col: {mid_c}")

            print(f"")

            if matrix[mid_r][mid_c] == target:
                return True
            elif matrix[mid_r][mid_c] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False