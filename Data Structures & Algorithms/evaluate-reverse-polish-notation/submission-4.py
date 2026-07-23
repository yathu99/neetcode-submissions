class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        resVal=None
        operators={'*','/','+','-'}
        ptr=0
        while(ptr<len(tokens)):
            if(len(tokens)==1):
                return int(tokens[0])
            if(tokens[ptr] in operators):
                curOp=tokens.pop(ptr)
                lastVal=tokens.pop(ptr-1)
                initVal=tokens.pop(ptr-2)
                ptr-=2
                if(curOp=="*"):
                    tokens.insert(ptr,int(initVal)*int(lastVal))
                elif(curOp=="/"):
                    tokens.insert(ptr,int(initVal)/int(lastVal))
                elif(curOp=="+"):
                    tokens.insert(ptr,int(initVal)+int(lastVal))
                elif(curOp=="-"):
                    tokens.insert(ptr,int(initVal)-int(lastVal))
            else:
                ptr+=1
        return int(tokens[0])
        
