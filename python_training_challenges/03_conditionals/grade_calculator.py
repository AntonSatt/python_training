def get_letter_grade(score):
    """Convert numerical score to letter grade"""
    # TODO: Fix the conditional logic
    if score > 90:
        return "A"
    elif score > 80:
        return "B"
    elif score > 70:
        return "C"
    elif score > 60:
        return "D"
    else:
        return "F"


if __name__ == "__main__":
    score = 85
    grade = get_letter_grade(score)
    print(f"Score: {score}, Grade: {grade}")
