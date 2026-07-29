class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = ""
        reverse = ""

        for letter in s:
            if letter.isalnum():
                forward = forward + letter.lower()

        for letter in reversed(s):
            if letter.isalnum():
                reverse = reverse + letter.lower()
      
        return forward == reverse