class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, answer = 0, 0
        perm_in = False
        if len(s1) > len(s2):
            return False
        if len(s1) == len(s2):
            if set(s1) == set(s2):
                return True

        for r in range(len(s1), len(s2)):
            perm_in = sorted(s1) == sorted(s2[l:l+len(s1)])
            while not perm_in and l<r:
                l += 1
                perm_in = sorted(s1) == sorted(s2[l:l+len(s1)])
                if perm_in:
                    return True

        return perm_in