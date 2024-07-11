class Solution:
    def maxArea(self, height) -> int:
        """
        Time Complexity is O(N), space complexity is O(1)
        :param height:
        :return:
        """
        max_water = 0
        i = 0
        j = len(height) - 1
        while i < j:
            width = j - i
            current_height = min(height[i], height[j])
            current_water = width * current_height
            max_water = max(max_water, current_water)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_water


if __name__ == '__main__':
    test_solution = Solution()
    # print(test_solution.select_s("abca"))
    s = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    test_solution.maxArea(s)
