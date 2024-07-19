class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        """
        Time Complexity is O(N**3), space complexity is O(N)
        :param nums:
        :param target:
        :return:
        """
        nums.sort()
        result_list = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # 跳过重复元素
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue  # 跳过重复元素
                left, right = j + 1, len(nums) - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        result_list.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1  # 跳过重复元素
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1  # 跳过重复元素
                        left += 1
                        right -= 1

        return result_list


if __name__ == '__main__':
    test_solution = Solution()
    nums = [2, 2, 2, 2, 2]
    # print(nums[2:3])
    target = 8
    print(test_solution.fourSum(nums, target))
