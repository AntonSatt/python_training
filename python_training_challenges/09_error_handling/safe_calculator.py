def safe_divide(a, b):
    """Safely divide two numbers, handling division by zero"""
    # TODO: Add error handling for division by zero
    return a / b


def safe_convert_to_int(value):
    """Safely convert a value to integer"""
    # TODO: Add error handling for invalid conversions
    return int(value)


def safe_get_element(lst, index):
    """Safely get an element from a list"""
    # TODO: Add error handling for index out of range
    return lst[index]


if __name__ == "__main__":
    print(f"Division: {safe_divide(10, 0)}")
    print(f"Conversion: {safe_convert_to_int('abc')}")
    print(f"Index: {safe_get_element([1, 2, 3], 5)}")
