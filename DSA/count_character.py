def count_character(input_string):
    # convert the string to lowercase
    input_string = input_string.lower()
    # remove space and special characters
    # create a dictionary to store the count of each character
    character_count = {}
    # loop through each character in the string
    for char in input_string:
        # remove space and special characters
        if(char >= 'a' and char <= 'z') or (char >= '0' and char <= '9'):
            # if the character is in the dictionary, increment the count
            if char in character_count:
                character_count[char] += 1
            else:
                # if the character is not in the dictionary, add it with count 1
                character_count[char] = 1
    
    # return the dictionary
    return character_count
    

print(count_character("Hello world"))
print(count_character("Hello world 123"))
print(count_character("Hello world 123!@#"))
print(count_character(""))