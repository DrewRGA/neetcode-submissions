class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleanS = ""

        for i in range(len(s)):
            if s[i].isalnum():
                cleanS = cleanS + s[i]

        left = 0
        right = len(cleanS) - 1

        while left < right:
            if cleanS[left] == cleanS[right]:
                left = left + 1
                right = right - 1
            else:
                return False
        return True