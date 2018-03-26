class Solution:
    """
    @param str: String
    @return: String
    """

    def convertPalindrome(self, str):
        # Write your code here
        if len(str) == 0 or str == None:
            return None


        length = len(str)
        end = 0



        for i in range(length-1, 0, -1):
            left=0
            right= i
            while left < right :
                if str[left]!= str[right]:
                    break
                left +=1
                right -=1
            if left >= right :
                end = i
                break

        appendstr= ""
        for s in str[end+1:length]:
            appendstr = s + appendstr
        return appendstr+str

obj=Solution()
print obj.convertPalindrome("fjwoei")












