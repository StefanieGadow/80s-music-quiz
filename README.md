# 80's Music Quiz

“80’s Music Quiz” is a Python terminal game which runs in the Code Institute mock terminal on Heroku. 
Users are asked 10 questions with four possible answers. Each correct answer adds one point to the user’s score.  

The live version can be found [here](https://music-quiz-b966ebd26850.herokuapp.com/).

![Mockup](/readme_images/mockup.png)

## How to play

The “80’s Music Quiz” is a classic multiple-choice quiz. The questions only have one topic.  

The player is asked 10 random questions with four possible answers. Each correct answer scores one point. The final score is displayed to the player at the end of the game.

## Site Owner Goals

- To provide the user with a simple game that is fun to play
- To present the user with an app that is easy to use
- To entice the user to return to the game to improve their 80’s music knowledge

## User stories

As a user, I want to:  
- Understand the rules of the game.
- Improve my 80’s music knowledge by being provided with the correct answers.
- Have a short “timeout” from my busy day.

## Logic Flow

In order to visualise the steps required in the game, I created a flow chart using Lucidchart. It proved to be very beneficial as it allowed me to gain an understanding of what functions were required for the game.

![Flowchart](/readme_images/flowchart.png)

## Features

### Existing features

- Welcome screen  
  The user is greeted by a welcome screen that shows the game’s name in ASCII text.
  ![ASCII logo](/readme_images/ascii-logo.png)  

- Rules  
  The rules of the game are displayed underneath the ASCII logo.
  ![Rules of the game](/readme_images/rules.png)  

- Random choice of questions  
  The quiz chooses 10 random questions out of 30 questions that were defined in the Google Sheets document.

- Accepts user input  
  The user must input a number corresponding to the answer after each question.
  ![Example of user input](/readme_images/user-input.png)  

- Calculates a score  
  Each correct answer adds one point to the score. The player can achieve a maximum score of 10/10. The user will be presented with their final score after the 10th question is answered.
  ![Final score](/readme_images/final-score.png)  

- After the game, the user will be asked if they want to play again.  
  ![Play again screen](/readme_images/play-again.png)

- Input validation and error-checking  
  The player cannot enter answer options lower than 1 or higher than 4.
  The player must enter numbers to choose an answer.
  ![Input validation for questions](/readme_images/validate-answer.png)  

  When the player is asked if they want to play again, the quiz only accepts “yes” or “no”.
  ![Input validation for play again question](/readme_images/invalid-play.png)

### Future features

- Add more questions to the document to encourage playing several rounds.
- Create easy, medium, and hard difficulty levels to make the game more interesting.

