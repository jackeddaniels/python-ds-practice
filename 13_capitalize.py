def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    listified_phrase = list(phrase)

    listified_phrase[0] = listified_phrase[0].upper()

    return ''.join(listified_phrase)


