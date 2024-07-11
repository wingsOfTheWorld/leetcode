class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Time Complexity is O(M+N), space complexity is O(1)
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        nums1[:p2 + 1] = nums2[:p2 + 1]
        print(p1, p2, p)
        print(nums1)


if __name__ == '__main__':
    test_solution = Solution()
    # print(test_solution.select_s("abca"))
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [4, 5, 6]
    n = 3
    test_solution.merge(nums1, m, nums2, n)