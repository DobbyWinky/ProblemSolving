def solution(S):
    stack=[]
    for s in S:
        if len(stack)==0:
            stack.append(s)
            continue
        if s=='(' or s=='{' or s=='[':
            stack.append(s)
            continue
        if s=='}' and (len(stack)==0 or stack[-1]!='{'):
            return 0
        if s==')' and (len(stack)==0 or stack[-1]!='('):
            return 0
        if s==']' and (len(stack)==0 or stack[-1]!='['):
            return 0
        else:
            stack.pop()
    if len(stack)==0:
        return 1
    return 0
