class Solution:
    def findLongestWord(self, s: str, dictionary) -> str:
        """
        Time Complexity is O(S*D), space complexity is O(1)
        :param s:
        :param dictionary:
        :return:
        """
        longest_word = ""
        i = 0
        while i < len(dictionary):
            j = 0
            k = 0
            while j < len(s) and k < len(dictionary[i]):
                if dictionary[i][k] == s[j]:
                    k += 1
                j += 1
            if k == len(dictionary[i]):
                if len(dictionary[i]) > len(longest_word) or (len(dictionary[i]) == len(longest_word) and dictionary[i] < longest_word):
                    longest_word = dictionary[i]
            i += 1
        return longest_word




if __name__ == '__main__':
    test_solution = Solution()
    s = "abpcplea"
    dictionary = ["ale", "apple", "monkey", "plea"]
    test_solution.findLongestWord(s, dictionary)