mystr = input()
bracketstack = []
def isbalanced(mystr):
    for i in mystr:
        if i == "(":
            bracketstack.append(i)
        elif i == "[":
            bracketstack.append(i)
        elif i =="{":
            bracketstack.append(i)
        elif i =="}":
            if len(bracketstack) == 0: return False
            if bracketstack[-1] == "{":
                bracketstack.pop(-1)
        elif i == "]":
            if len(bracketstack) == 0: return False
            if bracketstack[-1] == "[":
                bracketstack.pop(-1)
        elif i == ")":
            if len(bracketstack) == 0: return False
            if bracketstack[-1] == "(":
                bracketstack.pop(-1)
    if len(bracketstack) == 0:
        return True
    else: return False

a = isbalanced(mystr)
if a:
    print("YES")
else: print("NO")