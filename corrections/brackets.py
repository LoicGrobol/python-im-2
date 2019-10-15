openings = ("{", "[", "(")
closings = ("}", "]", ")")
match = dict(zip(closings, openings))

expression = input()

stack = []

for c in expression:
    # It's always correct to open a bracket
    if c in openings:
        stack.append(c)
    else:
        # This avoids a double lookup
        matching = match.get(c, None)
        # We only care about brackets
        # (This could be avoided in 3.8 using the walrus operator and an elif
        # instead of else)
        if matching is None:
            continue
        #  At this point, we are sure that c is a closing bracket
        # Fail if the stack is empty
        if not stack:
            print("false")
            break
        #  The opening bracket we encountered last
        # Either it matches and we will remove it or it doesn't and everything
        # fails so popping it is not an issue
        last = stack.pop()
        if last != matching:
            print("false")
            break
# This is a good example of how the else statement for for loops works but in
# the real world, wrapping it in a function and escaping with return or using a
# sentinel value is better practice
else:
    # Detects unclosed but correctly nested brackets
    if stack:
        print("false")
    else:
        print("true")
