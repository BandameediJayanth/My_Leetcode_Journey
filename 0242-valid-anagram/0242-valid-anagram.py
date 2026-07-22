from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t) #Counter creates a hashtable of the given string and the == operator check if both the hashtables are equal or not O(n) TC and O(n) SC
