import gspread
from google.oauth2.service_account import Credentials
import random
import os


class MusicQuizGame:
    """
    This class represents the 80's Music Quiz game. It allows players to
    participate in a quiz where they answer questions about music from the
    1980s. Players are presented with a set of questions, select answers,
    and receive scores based on their accuracy.
    """
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

    def __init__(self):
        self.score = 0

    def print_logo(self):
        """
        Display the ASCII logo for the Music Quiz.
        """

        logo = (
            " ****   ****   **       *     *             *          *****"
            "        *\n"
            "*    * *    *  *        **   **                       *     *\n"
            "*    * *    * *  ***    * * * * *   *  ***  *  ****   *     * "
            "*   * * *****\n"
            " ****  *    *   *       *  *  * *   * *     * *       *     * "
            "*   * *    *\n"
            "*    * *    *    ***    *     * *   *  ***  * *       *   * * "
            "*   * *   *\n"
            "*    * *    *       *   *     * *   *     * * *       *    * "
            " *   * *  *\n"
            " ****   ****    ****    *     *  ***  ****  *  ****    **** * "
            " ***  * *****"
        )
        print(logo)

    def display_rules(self):
        """
        Display the rules for the Music Quiz.
        """
        print("--------------------------------------------------------------"
              "------------------\n")
        print("Welcome to the 80's Music Quiz!")
        print("You will be asked 10 questions about 80's music.")
        print("Each correct answer earns you a point.")
        print("Are you an 80's music expert?\n")
        print("--------------------------------------------------------------"
              "------------------\n")

    def get_questions_from_sheet(self, data):
        """
        Fetch questions and correct answers from a Google Sheets document.
        """
        question_answer_pairs = [(row[0], row[5], row[1:5])
                                 for row in data[1:] if row[0] and row[5]]
        return question_answer_pairs

    def get_user_answer(self, possible_answers):
        """
        Get the user's answer and validate it.
        Args: possible_answers (list): List of possible answers to the
        question.
        Returns: int: The user's selected answer as an option number.
        """
        while True:
            try:
                user_answer = int(input("\nYour answer (enter the option"
                                        " number): \n"))
                if 1 <= user_answer <= len(possible_answers):
                    return user_answer
                else:
                    print("Please enter a valid option number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def main_quiz(self, question_answer_pairs):
        """
        Run the main quiz loop, asking the user 10 questions and evaluate their
        answers.
        Args: question_answer_pairs (list): A list of tuples containing
        question, possible answers and correct answer.
        Returns: int: The user's final score, indicating how many questions
        they have answered correctly.
        """
        num_questions = 10
        random.shuffle(question_answer_pairs)

        for i in range(num_questions):
            question, correct_answer, possible_answers = (
                question_answer_pairs[i]
            )
            print(f"{question}\n")
            random.shuffle(possible_answers)

            for i, ans in enumerate(possible_answers, 1):
                print(f"{i}. {ans}")

            user_answer = self.get_user_answer(possible_answers)

            if user_answer == possible_answers.index(correct_answer) + 1:
                print("\nCorrect!")
                self.score += 1
            else:
                print(f"\nThe correct answer is: {correct_answer}")
            print("-----------------------------------------------------------"
                  "---------------------\n")
        return self.score

    def play_again(self):
        """
        Ask the user if they want to play the quiz again.
        Returns True if the user wants to play again, False otherwise.
        """
        while True:
            continue_play = input("Do you want to play again? (yes/no):\n"
                                  " ").strip().lower()
            if continue_play == "yes":
                return True
            elif continue_play == "no":
                return False
            else:
                print('Please enter "yes" or "no".')

    def play(self):
        """
        Start the Music Quiz game.
        This method initiates the game loop, where players are presented with
        questions, their answers are evaluated, and scores are calculated.
        Players can choose to play again or exit the game.
        """
        self.print_logo()
        self.display_rules()

        while True:
            question_answer_pairs = (
                self.get_questions_from_sheet(MusicQuizGame.data)
            )
            self.score = self.main_quiz(question_answer_pairs)
            print(f"Your final score: {self.score}/10!\n")

            if self.play_again():
                os.system("clear")
                print("Great! Let's play again!\n")
                print("------------------------------------------------------"
                      "--------------------------\n")
            else:
                print("Thank you for playing. Goodbye!")
                break


def main():
    """
    Start the 80's Music Quiz game.
    This function initializes a new game instance and starts the game loop.
    """
    player1 = MusicQuizGame()
    player1.play()


main()
