class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        Time Complexity is O(N), space complexity is O(N)
        :param nums1:
        :param nums2:
        :return:
        """
        hash_map = {}
        for i in nums1:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1
        intersection_array = []
        for j in nums2:
            if j in hash_map and hash_map[j] >= 1:
                hash_map[j] -= 1
                intersection_array.append(j)
        return intersection_array


if __name__ == '__main__':
    test_solution = Solution()
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(test_solution.intersect(nums1, nums2))