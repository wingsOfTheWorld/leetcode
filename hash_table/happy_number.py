class Solution:
    def isHappy(self, n: int) -> bool:
        """

        :param n:
        :return:
        """
        def get_next(num):
            return sum(int(digit) ** 2 for digit in str(num))

        seen = []
        while n != 1 and n not in seen:
            if n not in seen:
                seen.append(n)
            n = get_next(n)

        return n == 1


if __name__ == '__main__':
    test_solution = Solution()
    n = 19
    print(test_solution.isHappy(n))
