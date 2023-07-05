#!/usr/bin/python3
"""4. Text indentation

a function that prints a text with 2 new lines after
each of these characters: ., ? and :

Prototype: def text_indentation(text):
text must be a string, otherwise raise a TypeError exception with
the message text must be a string
There should be no space at the beginning or at the end of
each printed line"""


def text_indentation(text):
    """
    function name: text_indentation
    arguments: text - string
    prints a text with 2 new lines after each of
    these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    my_text = ""
    delim = {'.', '?', ':'}
    for char in text:
        if char in delim:
            my_text += char + "\n\n"
        else:
            my_text += char
    lines = my_text.splitlines()
    my_text = '\n'.join(line.lstrip() for line in lines)
    if my_text and my_text[-1] == '\n':
        my_text = my_text[:-1]
    print(my_text)
