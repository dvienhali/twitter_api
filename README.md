# A Python script to manage Twitter API

This script is intended for educational and practice purposes. It demonstrates how to interact with the Twitter API to look up tweets from a user's timeline and save them to a CSV file. Before using this script, please read and understand Twitter's Development Terms and Conditions, as this script interacts with Twitter API.


# Getting Started

1. Clone this repository to your local machine.
2. Make sure you have Python 3.x installed.
3. Install the required dependencies using the following command:
   pip install requests
4. Obtain your Twitter API Bearer Token and set it as the value of the 'BEARER_TOKEN' environment variable.
   You can set the environment variable using the following command
   export 'BEARER_TOKEN'='<your_bearer_token>'
5. Modify the main function in the script to specify the user ID and the desired exclude option (retweets, replies,     etc.).
6. Run the script:
   python3 run.py


# Reference 

For more info please refer to Twitter Developer Documentation at:
  https://developer.twitter.com/
