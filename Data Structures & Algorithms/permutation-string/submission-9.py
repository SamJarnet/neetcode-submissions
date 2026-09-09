class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, answer = 0, 0
        if len(s1) > len(s2):
            return False

        window, target = {}, {}
        for i in range(0, len(s1)):
            target[s1[i]] = target.get(s1[i], 0) + 1
        for r in range(len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1
            if r - l + 1 > len(s1):
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    window.pop(s2[l])
                l += 1
            if r - l + 1 == len(s1):
                if window == target:
                    return True
        return False