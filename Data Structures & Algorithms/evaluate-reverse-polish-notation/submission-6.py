class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])
        operator_count = 0
        for i in range(0, len(tokens)):
            stack.append(tokens[i])
            if not tokens[i].lstrip('-').isnumeric():

                operator = stack.pop()
                snd = int(stack.pop())
                fst = int(stack.pop())
                if operator == '+':
                    stack.append(fst + snd)
                elif operator == '-':
                    stack.append(fst - snd)
                elif operator == '*':
                    stack.append(fst * snd)
                else:
                    stack.append(int(fst / snd))
        return stack[0] 