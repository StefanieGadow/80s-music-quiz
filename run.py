import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("music_quiz")


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





def main():
    print_logo()


main()
