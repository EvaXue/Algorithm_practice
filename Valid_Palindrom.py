##lintcode 415. Valid Palindrome

class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """

    def isPalindrome(self, s):
        # write your code here
        ##consider the null value
        if s is None or len(s) == 0:
            return True
        l = 0
        r = len(s) - 1
        s = s.lower()
        while l < r:
            while s[l].isalpha()==False and s[l].isdigit()==False:
                l = l + 1
                if l>r:
                    return True
            while s[r].isalpha()==False and s[r].isdigit()==False:
                r = r - 1
                if r<l:
                    return True
            if l < r and s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True

str="A man, a plan, a canal: Panamaew"
obj=Solution()
print (obj.isPalindrome(str))
