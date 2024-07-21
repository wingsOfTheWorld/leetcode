class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Time Complexity is O(Log(X)), space complexity is O(1)
        :param x:
        :return:
        """
        if x < 2:
            return x

        left, right = 2, x // 2

        while left <= right:
            mid = left + (right - left) // 2
            num = mid * mid

            if num == x:
                return mid
            elif num < x:
                left = mid + 1
            else:
                right = mid - 1

        return right


if __name__ == '__main__':
    test_solution = Solution()
    x = 2147395600
    print(test_solution.mySqrt(x))
