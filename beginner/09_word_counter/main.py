STOP_WORDS = {
    "the", "a", "an", "is", "in", "of", "and", "or", "to", "it",
    "was", "he", "she", "they", "we", "i", "be", "that", "this",
    "with", "at", "by", "from", "on", "are", "for", "as", "but",
}

print("Paste your text (press Enter twice when done):")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

text = " ".join(lines)

words = text.split()
total_words = len(words)
total_chars_with_spaces = len(text)
total_chars_no_spaces = len(text.replace(" ", ""))
sentences = sum(text.count(p) for p in ".!?")

word_counts = {}
for word in words:
    clean = word.strip(".,!?;:\"'").lower()
    if clean and clean not in STOP_WORDS:
        word_counts[clean] = word_counts.get(clean, 0) + 1

unique_words = len(set(w.strip(".,!?;:\"'").lower() for w in words if w))
top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:5]

print("\n--- Analysis ---")
print(f"Words          : {total_words}")
print(f"Characters     : {total_chars_with_spaces} ({total_chars_no_spaces} without spaces)")
print(f"Sentences      : {sentences}")
print(f"Unique words   : {unique_words}")

print("\nTop 5 words:")
for rank, (word, count) in enumerate(top_words, 1):
    print(f"  {rank}. {word:<12} — {count}")
