class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        """
        Time Complexity is O(N), space complexity is O(N)
        :param nums:
        :param indexDiff:
        :param valueDiff:
        :return:
        """
        bucket = {}
        bucket_size = valueDiff + 1
        for index, num in enumerate(nums):
            bucket_key = num // bucket_size
            if bucket_key in bucket:
                return True
            elif (bucket_key - 1 in bucket) and (abs(bucket[bucket_key - 1] - num) <= valueDiff):
                return True
            elif (bucket_key + 1 in bucket) and (abs(bucket[bucket_key + 1] - num) <= valueDiff):
                return True
            bucket[bucket_key] = num

            if index >= indexDiff:
                del bucket[nums[index - indexDiff] // bucket_size]
        return False


if __name__ == '__main__':
    test_solution = Solution()
    nums = [1, 5, 9, 1, 5, 9]
    indexDiff = 2
    valueDiff = 3
    print(test_solution.containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff))
