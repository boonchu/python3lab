templates = iter('(){}[]')
parens = dict(zip(templates, templates))
end_parens = parens.values()

def bl(strcmp):
    stack = []
    for c in strcmp:
        d = parens.get(c)
        if d:
            stack.append(d)
        elif c in end_parens:
            if not stack or c != stack.pop():
                return False
    return not stack

print bl('([])')
print bl('[]{}')

print bl('([)]')
print bl('](){')

print bl('(())')
