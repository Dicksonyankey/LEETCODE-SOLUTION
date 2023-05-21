def isValid(s: str) -> bool:
    stack = []
    lookups = {")": "(", "}": "{", "]": "["}

    for p in s:
        if p in lookups:
            if stack and stack[-1] == lookups[p]:
                stack.pop()
            else:
                return False
        else:
            stack.append(p)
    return True if not stack else False
