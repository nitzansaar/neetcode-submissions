class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       anagrams = []
       for s in strs: #go through each string
        for i in range(len(anagrams)): # go through each anagram
            if self.isAnagram(s, anagrams[i][0]): # only check the first one cause they are the same
                anagrams[i].append(s) # if anagram add to the list
                break
        else:
            anagrams.append([s])
       return anagrams 

            



    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        countS = defaultdict(int)
        for char in s:
            countS[char] += 1
        for char in t:
            if char not in countS:
                return False
            countS[char] -= 1
            if countS[char] == 0:
                del countS[char]
        return len(countS) == 0