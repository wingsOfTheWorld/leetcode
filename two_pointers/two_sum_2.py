class Solution:
    def twoSum(self, numbers, target):
        """
        Time Complexity is O(N)
        :param numbers:
        :param target:
        :return:
        """
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i+1, j+1]


if __name__ == '__main__':
    test_solution = Solution()
    a_list = [0, 0, 1, 1, 2, 3]
    print(test_solution.twoSum(a_list, 1))
