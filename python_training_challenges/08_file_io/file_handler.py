def read_file(filename):
    """Read the contents of a file"""
    # TODO: Fix the implementation
    file = open(filename, 'r')
    content = file.read
    return content


def write_file(filename, content):
    """Write content to a file"""
    # TODO: Fix the implementation
    file = open(filename, 'w')
    file.write(content)


def count_lines(filename):
    """Count the number of lines in a file"""
    # TODO: Fix the implementation
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines


if __name__ == "__main__":
    # Create a test file
    write_file('test.txt', 'Line 1\nLine 2\nLine 3')
    
    content = read_file('test.txt')
    print(f"Content: {content}")
    print(f"Lines: {count_lines('test.txt')}")
