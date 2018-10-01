def verify_parentheses(parentheses_string: str) -> bool:
    """Takes input string of only '{},[],()' and evaluates to True if valid."""
    open_parentheses = []
    valid_parentheses_set = {'(', ')', '[', ']', '{', '}'}
    parentheses_pairs = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }

    if len(parentheses_string) % 2 != 0:
        return False
    for character in parentheses_string:
        if character not in valid_parentheses_set:
            raise ValueError("Only parentheses may be part of input string.")
        if character in {'(', '[', '{'}:
            open_parentheses.append(character)
        if character in {')', ']', '}'}:
            if len(open_parentheses) == 0:
                return False
            elif open_parentheses[-1] != parentheses_pairs[character]:
                return False
            del open_parentheses[-1]
    if len(open_parentheses) > 0:
        return False
    return True


if __name__ == '__main__':
    first_example = verify_parentheses('(())}))')
    print(first_example)
    second_example = verify_parentheses('))((')
    print(second_example)
    third_example = verify_parentheses('([])')
    print(third_example)
    fourth_example = verify_parentheses('''([][])''')
    print(fourth_example)
    fifth_example = verify_parentheses(')(())()(')
    print(fifth_example)
    sixth_example = verify_parentheses('')
    print(sixth_example)
    seventh_example = verify_parentheses('[[[[[[[[[[]]]]]]]]]]()()')
    print(seventh_example)
    eighth_example = verify_parentheses('((')
    print(eighth_example)
    ninth_example = verify_parentheses('))')
    print(ninth_example)
