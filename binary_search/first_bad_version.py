# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Time Complexity is O(Log(N)), space complexity is O(1)
        :param n:
        :return:
        """
        left = 1
        right = n
        while left < right:
            middle = left + (right - left) // 2
            if isBadVersion(middle) == False and isBadVersion(middle + 1) == True:
                return middle + 1
            elif isBadVersion(middle) == False and isBadVersion(middle + 1) == False:
                right = middle
            else:
                left = middle
        return right


if __name__ == '__main__':
    test_solution = Solution()
    n = 5
    bad = 4
    test_solution.firstBadVersion(n)
