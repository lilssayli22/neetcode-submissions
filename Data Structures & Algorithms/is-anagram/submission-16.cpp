class Solution {
public:
    bool isAnagram(string s, string t) {
        std::map<char, int> m1;
        std::map<char, int> m2;
        for (int i=0;i<s.size();i++){
            m1[s[i]]=0;
        }
        for (int i=0;i<t.size();i++){
            m2[t[i]]=0;
        }
        for (int i=0;i<s.size();i++){
            m1[s[i]]+=1;
        }
        for (int i=0;i<t.size();i++){
            m2[t[i]]+=1;
        }
        if (m1 == m2){
            return true;
        }
        return false;
    }
};
