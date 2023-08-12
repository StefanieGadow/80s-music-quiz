import gspread
from google.oauth2.service_account import Credentials
import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("music_quiz")

questions = SHEET.worksheet("questions")
data = questions.get_all_values()


def print_logo():
    """
    Display the ASCII logo for the Music Quiz.
    """

    logo = r"""
     ****   ****   **        *     *             *           *****        *        
    *    * *    *  *         **   **                        *     *          
    *    * *    * *  ***     * * * * *   *  ***  *  ****    *     * *   * * *****  
     ****  *    *   *        *  *  * *   * *     * *        *     * *   * *    *   
    *    * *    *    ***     *     * *   *  ***  * *        *   * * *   * *   *   
    *    * *    *       *    *     * *   *     * * *        *    *  *   * *  *     
     ****   ****    ****     *     *  ***  ****  *  ****     **** *  ***  * *****
    """
    print(logo)


def display_rules():
    """
    Display the rules for the Music Quiz.
    """
    print("----------------------------------------------------")
    print("Welcome to the 80's Music Quiz!")
    print("You will be asked 10 questions about 80's music.")
    print("Each correct answer earns you a point.")
    print("Are you an 80's music expert?")
    print("----------------------------------------------------")


def get_questions_from_sheet(data):
    """
    Fetch questions and correct answers from a Google Sheets document.
    """
    question_answer_pairs = [(row[0], row[5], row[1:5]) 
    for row in data[1:] if row[0] and row[5]]
    return question_answer_pairs


def get_user_answer(possible_answers):
    """
    Get the user's answer and validate it.
    """
    while True:
        try:
            user_answer = int(input("Your answer (enter the option numer): "))
            if 1 <= user_answer <= len(possible_answers):
                return user_answer
            else: print("Please enter a valid option number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main_quiz(question_answer_pairs):
    score = 0
    num_questions = 10
    random.shuffle(question_answer_pairs)

    for i in range(num_questions):
        question, correct_answer, possible_answers = question_answer_pairs[i]
        print(question)
       
        random.shuffle(possible_answers)

        for i, ans in enumerate(possible_answers, 1):
            print(f"{i}. {ans}")

        user_answer = get_user_answer(possible_answers)

        if user_answer == possible_answers.index(correct_answer) + 1:
            print("Correct!")
            score += 1
        else:
            print(f"The correct answer is: {correct_answer}")
        print("----------------------------------------------------")
    return score


def play_again():
    """
    Ask the user if they want to play the quiz again.
    Returns True if the user wants to play again, False otherwise.
    """
    while True:
        continue_play = input("Do you want to play again? (yes/no): ").strip().lower()
        if continue_play == "yes":
            return True
        elif continue_play == "no":
            return False
        else:
            print('Please enter "yes" or "no".')


def main():
    print_logo()
    display_rules()

    while True:
        question_answer_pairs = get_questions_from_sheet(data);
        score = main_quiz(question_answer_pairs)
        print(f"Your final score: {score}/10!")

        if play_again():
            print("Great! Let's play again!\n")
        else: 
            print("Thank you for playing. Goodbye!")
            break

main()
