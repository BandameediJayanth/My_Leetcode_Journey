class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        hm = {'(': ')', '{': '}', '[': ']'}

        for i in s:
            if i in hm:
                arr.append(i)
            else:
                if not arr or hm[arr[-1]] != i:
                    return False
                arr.pop()

        return len(arr) == 0