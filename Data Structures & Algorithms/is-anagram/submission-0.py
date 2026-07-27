class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        dictT = {}

        for letter in s:
            if letter in dictS:
                dictS[letter] = dictS[letter] + 1
            else:
                dictS[letter] = 1

        for letter in t:
            if letter in dictT:
                dictT[letter] = dictT[letter] + 1
            else:
                dictT[letter] = 1

        if dictS == dictT:
            return True
        else:
            return False