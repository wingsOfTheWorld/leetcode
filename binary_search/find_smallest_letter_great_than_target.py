class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        """
        Time Complexity is O(Log(N)), space complexity is O(1)
        :param letters:
        :param target:
        :return:
        """
        left = 0
        right = len(letters) - 1
        if letters[right] < target:
            return letters[0]
        if letters[left] > target:
            return letters[0]
        while left < right:
            middle = left + (right - left) // 2
            if letters[middle] == target:
                while letters[middle] == target:
                    middle += 1
                return letters[middle]
            elif letters[middle] < target:
                left = middle + 1
            else:
                right = middle
        return letters[right]


if __name__ == '__main__':
    test_solution = Solution()
    letters = ["e", "e", "e", "k", "q", "q", "q", "v", "v", "y"]
    print(letters[:2])
    target = "e"
    print(test_solution.nextGreatestLetter(letters, target))
