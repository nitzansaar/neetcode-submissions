class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        // now we know the strings are same length
        vector<int> counts (26, 0);
        for (int i; i < s.length(); i++) {
            counts[s[i] - 'a']++;
            counts[t[i] - 'a']--;
        }
        for (int val : counts) {
            if (val != 0) {
                return false;
            }
        }
        return true;
    }
};
