class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """

    def longestPalindrome(self, s):
        # write your code here
        maxLen = 1
        start = 0
        length = len(s)


        for i in range(1, length):
            low = i - 1
            high = i

            # Find the longest even length palindrome with center
            # points as i-1 and i.
            while low >= 0 and high < length and s[low] == s[high]:
                if high - low + 1 > maxLen:
                    start = low
                    maxLen = high - low + 1
                low -= 1
                high += 1


                # Find the longest odd length palindrome with center
                # point as i
            low = i - 1
            high = i + 1

            while low >= 0 and high < length and s[low] == s[high]:
                if high - low + 1 > maxLen:
                    start = low
                    maxLen = high - low + 1
                low -= 1
                high += 1
            print low
            print high
            print start
        return s[start:start + maxLen]


obj = Solution()
print obj.longestPalindrome('a')