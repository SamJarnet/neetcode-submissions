class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        seen = {}
        answer = 0
        for i in range(0, len(s)):
            if s[i] not in seen:
                seen[s[i]] = 1
            else:
                seen[s[i]] += 1
            num_of_replace = i-left-seen[max(seen, key=seen.get)]+1
            while num_of_replace > k:
                seen[s[left]] -= 1
                left += 1
                num_of_replace = i-left-seen[max(seen, key=seen.get)]+1

            answer = max(answer, i - left + 1)
        return answer