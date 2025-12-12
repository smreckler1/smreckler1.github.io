# CTI 110 Trivia Quiz Game

print("===================================")
print("       Welcome to CTI 110 Trivia       ")
print("===================================")

# Define questions, options, and answers

questions = [
{
"question": "What is the capital of France?",
"options": ["A. London", "B. Berlin", "C. Paris", "D. Rome"],
"answer": "C"
},
{
"question": "Which planet is known as the Red Planet?",
"options": ["A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"],
"answer": "A"
},
{
"question": "What is 5 + 7?",
"options": ["A. 10", "B. 12", "C. 14", "D. 11"],
"answer": "B"
}
]

score = 0

# Loop through each question

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    answer = input("Enter your answer (A/B/C/D): ").upper()
    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {q['answer']}.")

print(f"\nYou got {score} out of {len(questions)} correct!")
print("Thank you for playing CTI 110 Trivia!")
