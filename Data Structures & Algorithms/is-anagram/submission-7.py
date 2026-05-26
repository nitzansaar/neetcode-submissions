class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashy = defaultdict(int)
        for char in s:
            hashy[char] += 1
        for char in t:
            if char not in hashy:
                return False
            hashy[char] -= 1
            if hashy[char] == 0:
                del hashy[char]
        return len(hashy) == 0