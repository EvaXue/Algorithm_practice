class Solution:

    def longestPalindromeSubseq(self, s):
        hash={}

        for c in s:
            if c in hash:
                del hash[c]
            else:
                hash[c]=True

        remove = len(hash)
        if remove >0:
            remove -=1
        return len(s)-remove

obj=Solution()
print obj.longestPalindromeSubseq('fjwiowejfjio')


