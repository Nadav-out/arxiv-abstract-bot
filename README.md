# arXiv Abstract Link Bot

This Slack bot listens for messages containing arXiv PDF links and automatically replies with the corresponding arXiv abstract links. 
## Requirements

- Python 3.6+
- [slack-bolt](https://github.com/slackapi/bolt-python) and [slack-sdk](https://github.com/slackapi/python-slack-sdk) libraries
- [python-dotenv](https://github.com/theskumar/python-dotenv) library

## Installation

1. Clone the repository:
git clone https://github.com/Nadav-out/arxiv-abstract-bot.git
cd arxiv-abstract-bot
2. Install the required packages:
pip install slack-bolt slack-sdk python-dotenv
3. Create a `.env` file in the project directory and add your Slack app and bot tokens: 
`SLACK_APP_TOKEN=your_app_token SLACK_BOT_TOKEN=your_bot_token` 
Replace `your_app_token` and `your_bot_token` with the actual tokens from your Slack app.

## Usage

Run the bot:

python app.py

The bot will now listen for messages containing arXiv PDF links in all channels/groups it is invited to and automatically reply with the corresponding abstract links.


## License

[MIT](https://choosealicense.com/licenses/mit/)
