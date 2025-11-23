# Simple Quiz
# This program gives 5 multiple choice questions and ask the user for the answer.
# It marks the quiz and saves the score to a text file.
#Key Improvements Added:
#Enhanced input validation​ using regex
#Attempt limits​ (3 attempts per question)
#Better user feedback​ with remaining attempts
#Improved score file​ with percentage and timestamp
#Better formatting​ with separators and clear sections
import re

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

def validate_input(user_input):
    """Enhanced input validation with regex"""
    pattern = r'^[A-Da-d]$'
    if re.match(pattern, user_input.strip()):
        return True
    return False

def ask_question(question_data): 
    print("\n" + question_data["question"])

    for option in question_data["answers"]:
        print(option)

    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        answer = input("Put your answer (A, B, C, or D):  ").upper().strip()
        
        if validate_input(answer):
            if answer == question_data.get("correct_answer"):
                print("Correct!")
                return True
            else:
                correct_letter = question_data.get("correct_answer")
                correct_text = None
                for opt in question_data["answers"]:
                    if opt.startswith(correct_letter):
                        correct_text = opt
                        break
                if correct_text:
                    print(f"Incorrect. The correct answer is {correct_text}.")
                return False
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            if remaining_attempts > 0:
                print(f"Invalid input. Please enter A, B, C, or D. ({remaining_attempts} attempts remaining)")
            else:
                print("Maximum attempts reached. Moving to next question.")
                correct_letter = question_data.get("correct_answer")
                correct_text = None
                for opt in question_data["answers"]:
                    if opt.startswith(correct_letter):
                        correct_text = opt
                        break
                if correct_text:
                    print(f"The correct answer was {correct_text}.")
                return False

def run_quiz():
    questions = load_questions()
    score = 0
    total_questions = len(questions)
    
    for q in questions:
        correct = ask_question(q)
        if correct:
            score += 1
    return score, total_questions

def save_score(score, total):
    with open("quiz_score.txt", "w") as file:
        file.write(f"Score: {score}/{total}\n")
        file.write(f"Percentage: {(score/total)*100:.1f}%\n")
        file.write(f"Date: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

def main():
    print("Welcome to the Simple Quiz!")
    print("=" * 40)
    
    score, total = run_quiz()
    
    print(f"\n{'='*40}")
    print(f"Quiz Completed!")
    print(f"Your final score is {score} out of {total}.")
    print(f"Percentage: {(score/total)*100:.1f}%")
    print("=" * 40)
    
    save_score(score, total)
    print("Your score has been saved to quiz_score.txt. Thank you for playing!")

if __name__ == "__main__":
    main()
    

 
