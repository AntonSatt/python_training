def find_max(numbers):
    """Find the maximum value in a list"""
    # TODO: Fix the implementation
    max_val = 0
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


def remove_duplicates(items):
    """Remove duplicates from a list while preserving order"""
    # TODO: Fix the implementation
    return list(set(items))


def flatten_list(nested):
    """Flatten a nested list"""
    # TODO: Fix the implementation
    result = []
    for item in nested:
        result.append(item)
    return result


if __name__ == "__main__":
    numbers = [23, 45, 12, 45, 23, 8]
    print(f"Max: {find_max(numbers)}")
    print(f"Unique: {remove_duplicates([1, 2, 2, 3, 3, 4, 5])}")
    print(f"Flat: {flatten_list([[1, 2], [3, 4], [5, 6]])}")
