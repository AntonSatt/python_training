def count_words(text):
    """Count the frequency of each word in a text"""
    # TODO: Fix the implementation
    words = text.split()
    word_counts = {}
    
    for word in words:
        if word in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] = 1
    
    return word_counts


if __name__ == "__main__":
    text = "The quick brown fox"
    result = count_words(text)
    print(result)
