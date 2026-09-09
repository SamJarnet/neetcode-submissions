class Solution:
    def minWindow(self, s: str, t: str) -> str:
        answer, shortest, l = "", len(s)+1, 0
        window, target = {}, {}
        have = 0
        if len(t) > len(s):
            return ""

        for i in range(0, len(t)):
            target[t[i]] = target.get(t[i], 0) + 1
            
        need_count = len(target)

        for r in range(0, len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in target and window[s[r]] == target[s[r]]:
                have += 1
            within = have == need_count
            while within:
                length = r - l + 1
                if length <= shortest and within:
                    shortest = length
                    answer = s[l:r+1]
                
                char = s[l]
                window[char] -= 1
                if char in target and window[char] < target[char]:
                    have -= 1

                if window[char] == 0:
                    window.pop(char)

                l += 1

                within = have == need_count

        return answer