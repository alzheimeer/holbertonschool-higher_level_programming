#!/usr/bin/python3
"""Function that splits a text according to ., ?, and :"""


def text_indentation(text):
    """Args:
       text (str): the string of text to split
    """
    if not isinstance(text, str) or text is None or len(text) < 0:
        raise TypeError('text must be a string')
    datos = text.replace('?', '?pepe')
    datos1 = datos.replace('.', '.pepe')
    datos2 = datos1.replace(':', ':pepe')
    t = datos2.split('pepe')
    len1 = len(t)
    a = 0
    if (t[len1-1]) == "":
        len1 -= 1
    for i in t:
        a += 1
        i1 = i.strip()
        print(i1)
        if a < len1:
            print()
