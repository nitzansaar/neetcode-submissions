class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int nums_len = sizeof(nums) / nums[0];
        std::set<int> seen;
        for (int num : nums){
            if (seen.contains(num)){
                return true;
            }
            seen.insert(num);
        }
        return false;
    }
};