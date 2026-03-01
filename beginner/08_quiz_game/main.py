import random

questions = [
    {
        "question": "What is the capital of Japan?",
        "options": ["A) Beijing", "B) Seoul", "C) Tokyo", "D) Bangkok"],
        "answer": "C",
    },
    {
        "question": "How many sides does a hexagon have?",
        "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
        "answer": "B",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Venus", "B) Saturn", "C) Jupiter", "D) Mars"],
        "answer": "D",
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A) Go", "B) Au", "C) Ag", "D) Gd"],
        "answer": "B",
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A) Charles Dickens", "B) Jane Austen", "C) William Shakespeare", "D) Mark Twain"],
        "answer": "C",
    },
    {
        "question": "What is 12 × 12?",
        "options": ["A) 124", "B) 132", "C) 144", "D) 148"],
        "answer": "C",
    },
    {
        "question": "Which ocean is the largest?",
        "options": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
        "answer": "D",
    },
    {
        "question": "What language is primarily spoken in Brazil?",
        "options": ["A) Spanish", "B) Portuguese", "C) French", "D) English"],
        "answer": "B",
    },
]

random.shuffle(questions)
score = 0
total = len(questions)

print("=== Quiz Game ===\n")

for i, q in enumerate(questions, 1):
    print(f"Question {i}/{total}:")
    print(q["question"])
    for option in q["options"]:
        print(f"  {option}")

    answer = input("\nYour answer: ").strip().upper()
    if answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The answer was {q['answer']}.\n")

print(f"You scored {score} out of {total} — ", end="")
if score == total:
    print("Perfect score!")
elif score >= 6:
    print("Great job!")
elif score >= 4:
    print("Not bad!")
else:
    print("Keep studying!")
