class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        final = 0
        count = 0
        left = 0
        biggest = 0
        for i in range(0, len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1   
      
            seen.add(s[i])
            if len(seen) > final:
                final = len(seen)
        return final