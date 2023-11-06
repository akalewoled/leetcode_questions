class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operation(num1,op,num2):
            if op=="+":
                return num1 +num2
            if op=="-":
                return num1 -num2
            if op=="*":
                return num1 *num2
            if op=="/":
                return int(num1 /num2)
        stack=[]
        for i in tokens:
            if i.isnumeric():
                stack.append(int(i))
            elif i[0] == '-' and i[1:].isnumeric():
                stack.append(int(i[1:])*-1)

            else:
                if  len(stack)<2:
                    return (" NONE VLUE")
                else:
                    num2=stack[-1]
                    num1=stack[-2]
                    stack.pop()
                    stack.pop()
                    stack.append(operation(num1,i,num2))
        return stack[0]