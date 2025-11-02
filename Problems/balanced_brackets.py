def checkBracket(s:str) ->bool:
    stack = []
    for i in s:
        if i == "(" or i == "{" or i == "[":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            else:
                popped = stack[-1]
                stack.pop()
                if (popped == "(" and i == ")") or (popped == "{" and i == "}") or (popped == "[" and i == "]"):
                    continue
                else:
                    return False
    
    return len(stack) == 0

print(checkBracket("[{()}]"))
print(checkBracket("[{(]"))
print(checkBracket("[{(])"))
