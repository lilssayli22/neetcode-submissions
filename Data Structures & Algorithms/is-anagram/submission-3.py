class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        #inittialisatoin
        for i in s:
            dict1[i]=0
        for i in s:
            dict1[i]=dict1[i]+1
        dict2={}
        for i in t:
            dict2[i]=0
        for i in t:
            dict2[i]=dict2[i]+1
        for k in dict1.keys():
            if (k not in dict2.keys()):
                return False
            elif dict2[k]!=dict1[k]:
                return False
        for k in dict2.keys():
            if (k not in dict1.keys()):
                return False
            elif dict2[k]!=dict1[k]:
                return False            
        return True