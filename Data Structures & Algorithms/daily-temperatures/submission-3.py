class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        
        # étape 1 : compresser en runs (valeur, longueur, index de départ)
        runs = []
        i = 0
        while i < n:
            j = i
            while j + 1 < n and temperatures[j + 1] == temperatures[i]:
                j += 1
            runs.append((temperatures[i], i, j))  # (valeur, start, end)
            i = j + 1
        
        # étape 2 : pour chaque run, chercher le prochain run avec valeur strictement plus grande
        l = [0] * n
        for r_idx, (val, start, end) in enumerate(runs):
            # scan des runs suivants
            k = r_idx + 1
            while k < len(runs) and runs[k][0] <= val:
                k += 1
            
            if k < len(runs):
                target_day = runs[k][1]  # start du run trouvé
                for idx in range(start, end + 1):
                    l[idx] = target_day - idx
            # sinon reste à 0 (déjà initialisé)
        
        return l