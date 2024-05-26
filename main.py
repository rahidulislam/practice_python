class BracketChecker:

    
    def is_balanced(input_string):
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in input_string:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map:
                if not stack or stack.pop() != bracket_map[char]:
                    return False
        return not stack

if __name__ == "__main__":
    from input_brackets import BracketInput
    
    brackets = BracketInput()
    input_string = brackets.input_bracket()
    print(f"Input: {input_string}")
    
    is_balanced_result = "Balanced" if BracketChecker.is_balanced(input_string) else "Not balanced"
    print(is_balanced_result)
    print(BracketChecker.is_balanced(input_string))




