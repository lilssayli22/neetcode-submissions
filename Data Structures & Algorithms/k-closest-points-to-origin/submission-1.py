class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(a): 
            return (a[0]**2 + a[1]**2)**(1/2)
        def delete(q):
            try:
                m = 0
                for i in range(len(q)):
                    if distance(q[i])< distance(q[m]):
                        m = i
                item = q[m]
                del q[m]
                return item
            except IndexError:
                print("Queue empty.")
                exit()
        l = [] 
        for i in range(k):
            l.append(delete(points))
        return l 