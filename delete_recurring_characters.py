"""
Given string as input, delete any recurring char, return the new string.
"""
# First example - assumes sorted input string.
def remove_recurring_characters(sorted_string: str) -> str:
    """Returns string without recurring characters, sorted input required."""
    output_string = ''

    for index, char in enumerate(sorted_string):
        if index == 0:
            output_string += char
        else:
            if char != sorted_string[index - 1]:
                output_string += char
    return output_string


# Second example - we can NOT assume sorted input string.
# Note should have used set below.
def get_unique_characters(string: str) -> str:
    """Returns string with all recurring characters removed."""
    seen_characters = set()
    output_string = ''

    for char in string:
        if char not in seen_characters:
            seen_characters.add(char)
            output_string += char
    return output_string


# Third example - cannot assume sort, using set data structure.
def get_unique_characters_again(string: str) -> str:
    """Returns string with all recurring characters removed."""
    return ''.join(set(string.lower()))



# tests.
print(remove_recurring_characters('HelloMynameisJohnathanImcool'))

print(get_unique_characters('Hello My name is Johnathan         I''m cool.@@'))

print(get_unique_characters_again('Hello My name is Johnathan         I''m cool.@@'))
