class Solution:
    def f(self,x):
        dicti = {}
        for i in x:
            dicti[i]=0
        for i in x:
            dicti[i]+=1
        return dicti
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for  i in strs:
            o   = False
            for j in dict1.keys():
                if self.f(j) == self.f(i):
                    o=True
                    dict1[j].append(i)
                    break
            if o==False:
                dict1[i]=[i]
        res = []
        for i in dict1.values():
            res.append(i)
        return res