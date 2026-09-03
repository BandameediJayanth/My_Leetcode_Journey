class Solution:
    def uniformArray(self, A):
        x = [float('inf'), float('inf')]

        for a in A:
            x[a & 1] = min(x[a & 1], a)

        return x[1] < x[0] or x[1] == float('inf')