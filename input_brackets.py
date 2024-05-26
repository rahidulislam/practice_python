class BracketInput:

    def is_valid_input(self, input_string):
        for char in input_string:
            if char not in "{}[]()":
                return False
        return True

    def input_bracket(self):
        while True:
            input_string = input(
                "Please enter a string containing only curly braces {}, square brackets [], and parentheses (): ")
            if self.is_valid_input(input_string):
                print(f"Thank you for the valid input: {input_string}")
                break
            else:
                print(
                    "Invalid input. Only curly braces {}, square brackets [], and parentheses () are allowed. Please "
                    "try again.")
        return input_string
