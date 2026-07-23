class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators=['/','*','-','+']
        if(len(tokens)<2):
            return int(tokens[0])
        for x in tokens:
            if(x not in operators):
                stack.append(x)
            else:
                first=int(stack.pop())
                second=int(stack.pop())
                if(x == '*'):
                    stack.append((second*first))
                elif(x == '/'):
                    stack.append((second/first))
                elif(x == '+'):
                    stack.append((second+first))
                elif(x == '-'):
                    stack.append((second-first))
        return int(stack[0])