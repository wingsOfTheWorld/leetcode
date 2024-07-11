class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        Time Complexity is O(Sqrt(N)), space complexity is O(1)
        :param c:
        :return:
        """
        border = int(c ** 0.5) + 1
        i = 0
        j = border
        while j >= i:
            if i*i + j*j == c:
                return True
            elif i*i + j*j > c:
                j -= 1
            elif i*i + j*j < c:
                i += 1
        return False


if __name__ == '__main__':
    test_solution = Solution()
    print(test_solution.judgeSquareSum(1000000000))
