class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> hash;
        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if (hash.contains(diff)) {
                return {hash[diff], i};
            }
            hash.insert({nums[i], i});
        }
    }
};
