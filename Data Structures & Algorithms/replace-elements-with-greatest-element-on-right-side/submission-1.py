class Solution:
 def merge_sort(self,arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = self.merge_sort(arr[:mid])
    right = self.merge_sort(arr[mid:])
    return self.merge(left, right)

 def merge(self,left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
 def replaceElements(self, arr) :
    a = self.merge_sort(arr)
    s={}
    l=[]

    for i in arr :
        s[i]=0
    for i in arr :
         s[i]+=1
    i = 0
    while i <len(arr)-1:
        s[arr[i]]-=1
        if arr[i] != a[-1]:
            l.append(a[-1])
        else : 
            a.pop()
            while s[a[-1]] ==0:
                a.pop(-1)
            l.append(a[-1])
        i+=1
    l.append(-1)
    return l