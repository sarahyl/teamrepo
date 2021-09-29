class Solution(object):
    def numOfStrings(self, patterns, word):
        count = 0
        for pattern in patterns:
            if word.find(pattern) != -1:
                count = count + 1
        return count
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """