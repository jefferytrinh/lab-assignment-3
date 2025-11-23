#Simple Quiz
#This program gives 5 multiple choice questions and ask the user for the answer.
#It marks the quiz and saves the score to a text file.
def load_questions():
    return [
        {"question": "Which national team recently won the World Cup in 2022?",
         "answers": ["A) Brazil", "B) France", "C) Argentina", "D) Italy"],
         "correct_answer": "C"},

        {"question": "What is the capital of Canada?",
         "answers": ["A) Toronto", "B) Edmonton", "C) Ottawa", "D) Montreal"],
         "correct_answer": "C"},

        {"question": "What country is the Burj Khalifa located in?",
         "answers": ["A) Saudi Arabia", "B) UAE", "C) Qatar", "D) Oman"],
         "correct_answer": "B"},

        {"question": "Is Pluto a dwarf planet?",
         "answers": ["A) Yes", "B) No"],
         "correct_answer": "A"},

        {"question": "What Country does Asics originate from?",
         "answers": ["A) China", "B) South Korea", "C) Japan", "D) Vietnam"],
         "correct_answer": "C"},
    ]

def ask_question(question_data): 

    print("\n" + question_data["question"])

    for option in question_data["answers"]:
        print(option)

    while True:
#ask user for answer
        answer = input("Put your answer (A, B, C, or D):  ").upper().strip()
#check answer
        if answer in ["A", "B", "C", "D"]:
            if answer == question_data.get("correct_answer"):
                print("Correct!")
                return True
            else:
#identify the full text of the correct answer choice
                correct_letter = question_data.get("correct_answer")
                
                correct_text = None
                for opt in question_data["answers"]:
                    if opt.startswith(correct_letter):
                        correct_text = opt
                        break
#Display correct answer
                if correct_text:
                    print(f"Incorrect. The correct answer is {correct_text}.")
                return False
        else:
            print("Invalid input. Please enter A, B, C, or D.")

def run_quiz():
    questions = load_questions()
    score = 0
    total_questions = len(questions)
#ask each question in the quiz
    for q in questions:
        correct = ask_question(q)
        if correct:
            score += 1
    return score, total_questions

def save_score(score, total):
    with open("quiz_score.txt", "w") as file:
        file.write(f"Score: {score}/{total}\n")

def main():
    print("Welcome to the Simple Quiz!")
#Run quiz and get score
    score, total = run_quiz()
#display results
    print(f"\nYour final score is {score} out of {total}.")
#save score to file
    save_score(score, total)

    print("Your score has been saved to quiz_score.txt. Thank you for playing!")
#required to run main function
if __name__ == "__main__":
    main()
    

 