class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        """
        Time Complexity is O(N), space complexity is O(N)
        :param nums:
        :param k:
        :return:
        """
        hash_map = {}
        for index, num in enumerate(nums):
            if num not in hash_map:
                hash_map[num] = index
            else:
                if index - hash_map[num] <= k:
                    return True
                else:
                    hash_map[num] = index
        return False


if __name__ == '__main__':
    test_solution = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    print(test_solution.containsNearbyDuplicate(nums, k))

