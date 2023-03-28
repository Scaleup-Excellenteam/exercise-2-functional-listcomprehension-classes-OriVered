def group_by(func, iterable):
    """
    Groups the elements of an iterable based on the result of applying a given function on each element.

    Args:
        func (callable): A function to apply on each element of the iterable.
        iterable (iterable): An iterable containing the elements to be grouped.

    Returns:
        dict: A dictionary containing the grouped elements, with the keys being the result of applying the function on the elements
              and the values being a list of elements that correspond to the key.
    """
    result = {}
    for item in iterable:
        key = func(item)
        if key in result:
            result[key].append(item)
        else:
            result[key] = [item]
    return result


if __name__ == "__main__":
    group = group_by(len, ["hi", "bye", "yo", "try"])
    print(group)
