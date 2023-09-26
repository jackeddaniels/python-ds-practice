def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    swapped_str = ''

    for ltr in phrase:
        if ltr.lower() == to_swap.lower():
            swapped_str += ltr.swapcase()
        else:
            swapped_str += ltr

    return swapped_str