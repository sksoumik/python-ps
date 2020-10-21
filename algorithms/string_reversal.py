# 5 ways to reverse a string

import time


# method 2: loop
def string_reverse_1(input_string):
    """
    Function is used to reverse a string.
    
    Args:
      input_string (str): Input string.
    
    Returns:
      rev_string (str): reverse string 
    """

    rev_string = ""

    for char in input_string:
        rev_string = char + rev_string

    return rev_string


# method 2: recursion
def string_reverse_2(input_string):
    """
    Function is used to reverse a string.
    
    Args:
      input_string (str): Input string.
    
    Returns:
      rev_string (str): reverse string 
    """

    if input_string == "":
        return input_string
    else:
        return input_string[-1] + string_reverse_2(input_string[:-1])


# method 2: recursion
def string_reverse_2(input_string):
    """
    Function is used to reverse a string.
    
    Args:
      input_string (str): Input string.
    
    Returns:
      rev_string (str): reverse string 
    """

    if input_string == "":
        return input_string
    else:
        return input_string[-1] + string_reverse_2(input_string[:-1])



if __name__ == "__main__":
    input_string = "soumik"
    print(string_reverse_1(input_string))
    print(string_reverse_2(input_string))
