class Solution:
    def dailyTemperatures(self, temperatures):
        l = []

        for i in range(len(temperatures) - 1):
            j = 1

            while i + j < len(temperatures) and temperatures[i + j] <= temperatures[i]:
                j += 1

            if i + j == len(temperatures):
                j = 0

            l.append(j)

        l.append(0)
        return l