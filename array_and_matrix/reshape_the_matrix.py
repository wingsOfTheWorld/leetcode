import numpy as np


class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        """
        Time Complexity is O(Log(m*n)), space complexity is O(1)
        :param mat:
        :param r:
        :param c:
        :return:
        """
        if len(mat) < 1:
            return mat
        length = len(mat)
        columns = len(mat[0])
        if length * columns != r * c:
            return mat
        new_mat = [[] * i for i in range(r)]
        for i in range(length):
            for j in range(columns):
                # print(new_mat)
                new_mat[(i * columns + j) // c].append(mat[i][j])
        return new_mat


if __name__ == '__main__':
    test_solution = Solution()
    mat = [[1, 2], [3, 4], [5, 6]]
    r = 2
    c = 3
    print(test_solution.matrixReshape(mat, r, c))
    # print(np.array(mat).reshape(r, c).tolist())
