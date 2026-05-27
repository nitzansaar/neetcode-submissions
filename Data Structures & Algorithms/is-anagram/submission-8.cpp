class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        unordered_map<char, int> cChars;
        for (char c : s) {
            cChars[c]++;
        }
        for (char c : t) {
            if (cChars.find(c) == cChars.end()) {
                return false;
            }
            cChars[c]--;
            if (cChars[c] == 0) {
                cChars.erase(c);
            }
            
        }
        return cChars.empty();
    }
};
