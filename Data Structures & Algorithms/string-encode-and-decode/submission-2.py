class Solution:
    start_char = '!'
    def encode(self, strs: List[str]) -> str:
        #take a list of strings and encode it somehow into 
        #a decryptable single string
        res = ''
        for s in strs:
            res += (self.start_char + str(len(s)) + self.start_char + s)
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            i += 1
            j = i
            while s[j] != self.start_char:
                j+=1
            cur_len = int(s[i:j])
            j+=1
            res.append(s[j:j+cur_len])
            i = j+cur_len
        return res