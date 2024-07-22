class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Time Complexity is O(m * n), space complexity is O(1)
        :param matrix:
        :param target:
        :return:
        """
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        row = len(matrix[0])
        column = len(matrix)

        def get_row_index(matrix, target):
            left = 0
            right = column - 1
            while left < right:
                middle = left + (right - left) // 2
                # print(left, middle, right)
                if matrix[middle][0] <= target < matrix[middle + 1][0]:
                    return middle
                elif target < matrix[middle][0]:
                    right = middle - 1
                elif target >= matrix[middle + 1][0]:
                    left = middle + 1
            return right

        row_index = get_row_index(matrix, target)
        print(row_index)
        left_index = 0
        right_index = row - 1
        if left_index == right_index:
            if matrix[row_index][0] == target:
                return True
            else:
                return False
        while left_index < right_index:
            middle_index = left_index + (right_index - left_index) // 2
            print(left_index, middle_index, right_index)
            if matrix[row_index][middle_index] == target or matrix[row_index][middle_index + 1] == target or \
                    matrix[row_index][middle_index - 1] == target:
                return True
            elif matrix[row_index][middle_index] < target < matrix[row_index][middle_index + 1]:
                return False
            elif matrix[row_index][middle_index + 1] < target:
                left_index = middle_index + 1
            elif target < matrix[row_index][middle_index]:
                right_index = middle_index - 1
        # print(right_index)
        return False


if __name__ == '__main__':
    test_solution = Solution()
    matrix = [[1]]
    target = 1
    print(test_solution.searchMatrix(matrix, target))
