class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        std::unordered_map<char, int> counts;
        int n = sizeof(s) / sizeof('a');
        for (char c : s){
            if (counts.contains(c)) {
                counts[c]++;
            } else{
                counts.insert({c, 1});
            }
        }
        for (char c : t) {
            if (counts.contains(c)) {
                counts[c]--;
                if (counts[c] == 0) {
                    counts.erase(c);
                }
            }
        }
        return counts.size() == 0;
    }
};
