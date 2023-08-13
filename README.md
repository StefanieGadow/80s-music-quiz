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

## Google API

The questions, possible answers and correct answers are stored in a Google Sheet. The spreadsheet is accessed by the game through the Google Drive and Google Sheets APIs on the Google Cloud Platform.  

Credentials were generated and provided to allow access from the game to Google Sheets. These were added to the creds.json. The creds.json file was added to the .gitignore file to ensure the credentials were not pushed to the Github repository. The credentials were added to the Config Vars on Heroku to ensure they can be accessed when running the game.

## Data model

To use principles of Object-Oriented Programming, a MusicQuizGame class was created. This class is responsible for controlling the flow of the game. It contains methods for the general running of the game, such as displaying the ASCII logo, displaying rules, choosing questions, taking user guesses, displaying feedback on user guesses, updating the score and restarting the game.

By using a class, the game’s behaviour and data are encapsulated within instances of the class. Each player can have their game instance, allowing them to play independently without interfering with each other’s progress. This approach provides better organization, separation of concerns, and potential for code reusability and extensibility.

## Testing

### PEP8 Testing

The Python file has been passed through the CI Python Linter. There were no errors reported.

![Python Linter outcome](/readme_images/pep8.png)

### Input Testing

All user inputs were tested thoroughly to ensure all input data is handled correctly and appropriate feedback is given to the user. 

- Answer selection:
  User input that does not match one of the answer options is not accepted and returns an appropriate error message to the user.
- Play again selection:
  All input other than “yes” or “no” returns an appropriate error message to the user. It does not matter if the user uses lower or uppercase letters.

### Other Game Testing

The game was tested thoroughly to ensure the following features work as intended:
- The questions are randomised for each game. 
- The possible answers are randomised before they are displayed.
- The game ends after 10 questions and displays the final score to the user.
- The terminal clears if the user chooses to play again.
- The game was run on two devices simultaneously to ensure that multiple people could play the game at the same time.

All of the above tests were completed in my local terminal and also in the Heroku terminal.

## Libraries and Technologies Used

### Python libraries
	
- [random](https://docs.python.org/3/library/random.html?highlight=random#module-random): random is used to choose the 10 questions for the game and to randomize the possible answers for each question
- [os](https://docs.python.org/3/library/os.html?highlight=os#module-os): os.system is used to clear the terminal when the user wants to play again
- [gspread](https://pypi.org/project/gspread/): to allow communication with Google Sheets
- [google.oauth2.service_account](https://google-auth.readthedocs.io/en/stable/index.html): used to validate credentials and grant access to Google service accounts.

### Technologies

- [Github](https://github.com/): used for version control
- [Gitpod](https://gitpod.io/): used to develop the project and organise version control.
- [Heroku](https://heroku.com): used to deploy the live project
- [Lucidchart](https://lucid.app/): used to create the game flowchart
- [CI Python Linter](https://pep8ci.herokuapp.com/): used to validate the Python code
- [ASCII-Generator](https://ascii-generator.site/t/): used to create the ASCII logo

## Bugs

No remaining bugs.

## Deployment

The project was deployed via Heroku and can be found [here](https://music-quiz-b966ebd26850.herokuapp.com/).  

Before deploying to Heroku, pip3 freeze > requirements.txt was used to add all the dependencies required to the requirements.txt file. This is required for the game to run on Heroku.  

The following steps were then taken:

1.	Log in to Heroku or create an account.
2.	On the main page, click "Create New App".
3.	Enter a unique and meaningful app name.
4.	Next, select your region.
5.	Click on the Create App button.
6.	Click on the Settings Tab and scroll down to Config Vars.
7.	Click Reveal Config Vars, enter CREDS into the Key box and the content of the creds.json into the Value box, and click the Add button.
8.	Next, scroll down to the Buildpack section, click Add Buildpack select Python and click Save Changes.
9.	Repeat step 8 to add node.js. Note: The Buildpacks must be in the correct order. If not, click and drag them to move into the correct order.
10.	Scroll to the top of the page and choose the Deploy tab.
11.	Select Github as the deployment method.
12.	Confirm you want to connect to GitHub.
13.	Search for the repository name and click the connect button.
14.	Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
15.	Click View to view the deployed site.  

The site is now live and operational.

## Credits

The Code Institute walkthrough project “Love sandwiches” was used to set up the Google APIs and to deploy the project on Heroku.

[ChatGPT](https://chat.openai.com/) for the questions and answer options.
