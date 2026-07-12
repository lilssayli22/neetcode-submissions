class Solution:
    def reorderList(self, head):
        # 1. compter la longueur
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        # 2. avancer jusqu'au noeud n//2 - 1 pour couper juste après
        first = head
        for _ in range(n // 2 ):
            first = first.next
        
        second = first.next
        first.next = None  # coupe la première moitié
        
        # 3. reverser la deuxième moitié
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        second = prev
        
        # 4. merge alterné
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2