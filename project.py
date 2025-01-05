#QUIZE game using Python
def quiz_game():
    # List of questions, choices, and correct answers
    questions = [
        {
            "question": "What is the capital of India?",
            "choices": ["A) kathmandu", "B) Bihar", "C) Paris", "D) NewDelhi"],
            "answer": "D"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "choices": ["A) Earth", "B) Mars", "C) Venus", "D) Jupiter"],
            "answer": "B"
        },
        {
            "question": "Who wrote 'Muna Madan'?",
            "choices": ["A) Shakespeare", "B) Laxmi Parsad Devkota", "C) Austen", "D) Orwell"],
            "answer": "B"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "choices": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
            "answer": "D"
        }
    ]
    
    score = 0
    
    print("Welcome to the Quiz Game!")
    print("Please answer the following questions.\n")
    
    # Loop through each question
    for i, question in enumerate(questions, start=1):
        print(f"Q{i}: {question['question']}")
        for choice in question['choices']:
            print(choice)
        
        # Get the user's answer
        answer = input("Enter your choice (A/B/C/D): ").upper()
        
        # Check if the answer is correct
        if answer == question['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}.\n")
    
    # Show final score
    print(f"Your final score is {score}/{len(questions)}.")
    
    if score == len(questions):
        print("Excellent! You got all answers correct!")
    elif score >= len(questions) / 2:
        print("Good job! Keep learning!")
    else:
        print("Better luck next time!")

# Start the quiz game
quiz_game()
