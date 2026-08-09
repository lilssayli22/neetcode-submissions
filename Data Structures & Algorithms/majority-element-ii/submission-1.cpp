class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        std::map<int,int> a ;
        for (int i =0;i<nums.size();i++){
            a[nums[i]]+=1;
        }
        vector<int> l;
        for (auto i=a.begin();i!=a.end();i++){
            if (i->second > nums.size()/3){
                l.push_back(i->first);
            }
        }
        return l;
    }
};