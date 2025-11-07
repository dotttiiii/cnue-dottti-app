def display_question(question):
    print(f"Spell the word: {question}")

def display_result(is_correct):
    if is_correct:
        print("Correct!")
    else:
        print("Incorrect. Please try again.")