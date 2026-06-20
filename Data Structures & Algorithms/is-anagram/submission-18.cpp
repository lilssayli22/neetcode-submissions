class Solution {
public:
    bool isAnagram(string s, string t) {
    if (s.size() != t.size()) return false;
    
    std::map<char, int> m1;
    for (char c : s) m1[c]++;
    for (char c : t) m1[c]--;
    
    for (auto& [key, val] : m1) {
        if (val != 0) return false;
    }
    return true;
}
};
