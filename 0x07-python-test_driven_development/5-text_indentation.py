#!/usr/bin/python3
def text_indentation(text):
    """
    Function to print a text with two new lines
    after each of ., ? and : symbols.

    Parameters:
    text (str): Text string to modify and print

    Returns:
    No return value.
    Prints modified string to stdout.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ['.', '?', ':']:
        text = text.replace(delim, delim + '\n\n')

    lines = text.split('\n')

    for i in range(len(lines)):
        print(lines[i].strip())
