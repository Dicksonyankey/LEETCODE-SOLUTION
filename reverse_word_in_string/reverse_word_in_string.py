def reverseWords(s: str) -> str:
    # Solution one 
    return " ".join(s.split()[::-1])

    # Solution two
    word = s.split()
    reversed_word = word[::-1]
    reversed_word = " ".join(reversed_word)
    return reversed_word

    # Solution three
    word = ""
    new_list = []
    for i in range(len(s.split()),0, -1):
        new_list.append(s.split()[i-1])
    return " ".join(new_list)
