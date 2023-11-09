def remove_char_at(str, n):
    # Base case: if index is 0,
    # return string with first character removed
    if n == 0:
        return str[1:]
 
    # Recursive case: return first character
    # concatenated with result of calling function
    # on string with index decremented by 1
    return str[0] + remove_char_at(str[1:], n - 1)