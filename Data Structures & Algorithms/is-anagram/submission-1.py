class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charHash = {}
        for char in s:
            charHash[char] = charHash.get(char, 0) + 1
        for char in t:
            if char not in charHash:
                return False
            charHash[char] -= 1
            if charHash[char] == 0:
                del charHash[char]
        return len(charHash) == 0