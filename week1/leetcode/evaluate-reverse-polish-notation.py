class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operation = ['+','-','*','/']
        for i in range(len(tokens)):
            if tokens[i] in operation:
                val2 = stack.pop()
                val1 = stack.pop()

                if tokens[i] == "+":
                    stack.append(val1 + val2)
                elif tokens[i] == '-':
                    stack.append(val1 - val2)
                elif tokens[i] == '*':
                    stack.append(val1 * val2)
                elif tokens[i] == '/':
                    if val1 < 0 and val2 > 0 or val1 > 0 and val2 < 0:
                        stack.append(math.ceil(val1/val2))
                    else:
                        stack.append(val1//val2)
            else:
                stack.append(int(tokens[i]))
        
        return stack[0]