def sum_list(numbers):
    """Sum all numbers in a list"""
    # TODO: Fix the loop logic
    total = 0
    for i in range(len(numbers)):
        total = total + i
    return total


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    result = sum_list(numbers)
    print(f"Sum: {result}")
