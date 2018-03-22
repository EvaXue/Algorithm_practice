class Solution:
    """
    @param s: a string
    @return: nothing
    """

    def validPalindrome(self, s):
        # Write your code here
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return self.isPalindrome(s, l + 1, r) or self.isPalindrome(s, l, r - 1)
            else:
                l +=1
                r -=1
        return True

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l +=1
                r -=1
        return True


obj=Solution()
print (obj.validPalindrome('abcba'))