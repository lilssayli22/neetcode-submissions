class Solution {
public:
    int majorityElement(vector<int>& nums) {
        std::map<int, int> m;
        
        // Remplir la map - PAS BESOIN de boucle while!
        for (int i = 0; i < nums.size(); i++) {
            m[nums[i]]++;  // C'est tout!
        }
        
        // Chercher le majority element
        for (auto it = m.begin(); it != m.end(); ++it) {
            if (it->second > (int)nums.size() / 2) {
                return it->first;
            }
        }
        
        return -1;  // Jamais atteint
    }
};