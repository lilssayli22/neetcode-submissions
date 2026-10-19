class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        left = []   
        right = []  

        for a in asteroids:
            if a > 0:
                right.append(a)
            else:
                
                while right and right[-1] < abs(a):
                    right.pop()

                if right and right[-1] == abs(a):
                    right.pop()          
                elif not right:
                    left.append(a)       
                

        return left + right