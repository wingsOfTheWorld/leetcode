class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Time Complexity is O(m + n), space complexity is O(1)
        :param matrix:
        :param target:
        :return:
        """
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1

        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1

        return False


if __name__ == '__main__':
    test_solution = Solution()
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target = 7
    print(test_solution.searchMatrix(matrix, target))
