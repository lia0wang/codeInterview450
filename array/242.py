class Solution(object):
    def Solution1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        hash_map = {}
        for c in s:
            hash_map[c] = s.count(c)
        
        for c in t:
            if c not in hash_map.keys():
                return False
            if hash_map[c] != t.count(c):
                return False
        return True

    def Solution2(self, s, t):
        return sorted(s) == sorted(t)
    
s = "anagram"
t = "nagaram"
s2 = "rat"
t2 = "car"

solution = Solution()

print(solution.Solution2(s, t))
print(solution.Solution2(s2, t2))
