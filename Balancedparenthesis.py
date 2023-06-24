def is_balanced(parentheses):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}

    for bracket in parentheses:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if len(stack) == 0:
                return False
            last_opening_bracket = stack.pop()
            if bracket != bracket_pairs[last_opening_bracket]:
                return False

    return len(stack) == 0

input_string = input("Enter a combination of parentheses: ")
if is_balanced(input_string):
    print("balanced")
else:
    print("not balanced")