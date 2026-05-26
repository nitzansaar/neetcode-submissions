class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = {}
        for char in s:
            char_map[char] = char_map.get(char, 0) + 1
        for char in t:
            if char not in char_map:
                return False
            char_map[char] -= 1
            if char_map[char] == 0:
                del char_map[char]
        return len(char_map) == 0
