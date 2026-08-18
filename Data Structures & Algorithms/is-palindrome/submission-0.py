class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alphnum(w):
            return w.isalnum()
        test = filter(alphnum, s)
        filtered = list(test)
        head = 0
        tail = -1
        for i in range(0, len(filtered)):
            if filtered[head].lower() != filtered[tail].lower():
                return False
            head += 1
            tail -= 1
        return True