class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        seen = {}
        answer = 0
        maxf = 0
        for i in range(0, len(s)):
            seen[s[i]] = seen.get(s[i], 0) + 1
            maxf = max(seen[s[i]], maxf)
            num_of_replace = i-left-maxf+1
            while num_of_replace > k:
                seen[s[left]] -= 1
                left += 1
                num_of_replace = i-left-maxf+1

            answer = max(answer, i - left + 1)
        return answer