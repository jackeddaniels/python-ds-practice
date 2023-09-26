def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counts = {}
    highest_count = 0
    highest_associated_key = 0

    for num in nums:
        current_value = counts.get(num, 0)
        counts[num] = current_value + 1

        if current_value > highest_count:
            highest_count += 1
            highest_associated_key = num

    return highest_associated_key

