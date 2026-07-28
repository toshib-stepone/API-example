import random


QUESTIONS = {
    "What is the capital of France?": "paris",
    "What is 7 x 8?": "56",
    "What planet is known as the Red Planet?": "mars",
    "What is the largest ocean on Earth?": "pacific",
    "Who wrote 'Romeo and Juliet'?": "shakespeare",
}


def run_quiz():
    questions = list(QUESTIONS.items())
    random.shuffle(questions)

    score = 0
    total = len(questions)

    print("Welcome to the Quiz! Answer the following questions:\n")

    for i, (question, answer) in enumerate(questions, start=1):
        print(f"Q{i}: {question}")
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {answer.title()}\n")

    print("--- Quiz Finished ---")
    print(f"Your score: {score}/{total}")

    percentage = (score / total) * 100
    if percentage == 100:
        print("Perfect score! 🎉")
    elif percentage >= 60:
        print("Good job!")
    else:
        print("Better luck next time!")


def main():
    while True:
        run_quiz()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()