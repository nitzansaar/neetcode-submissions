class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
      std::set<int> numSet;
      for (int i = 0; i < nums.size(); ++i) {
        if (numSet.contains(nums[i])) {
            return true;
        }
        numSet.insert(nums[i]);
      } 
      return false;
    }
};