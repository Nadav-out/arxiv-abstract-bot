import os
import re
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import requests
from dotenv import load_dotenv

load_dotenv()

SLACK_APP_TOKEN = os.environ.get("SLACK_APP_TOKEN")
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")

app = App()

@app.event("message")
def process_message(body, say):
    # Ignore bot messages
    if "subtype" in body["event"] and body["event"]["subtype"] == "bot_message":
        return

    # Check if the message is from a public or private channel
    if body["event"]["channel_type"] not in ["channel", "group"]:
        return

    text = body['event']['text']

    pattern = r'arxiv.org/pdf/((?:\d+\.\d+v?\d*|[\w-]+)(?:/\d+)?)\.pdf'
    matches = re.finditer(pattern, text)

    found = False
    arxiv_links = set()

    for match in matches:
        arxiv_id = match.group(1)
        arxiv_link = 'https://arxiv.org/abs/{}'.format(arxiv_id)
        arxiv_links.add(arxiv_link)
        found = True

    # if found:
    #     response = "Ahoy there! Next time, consider sharing arXiv abstract links instead of PDFs. :wink:\nHere are the abstract links for your convenience: " + ', '.join(arxiv_links)
    #     say(response)
    if found:
        blocks = [
            {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Ahoy there! Next time, consider sharing arXiv abstract links instead of PDFs. :wink:"
            }
        }
    ]
    
    for link in arxiv_links:
        blocks.append({
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"• <{link}|{link}>"
                }
            ]
        })

    say(blocks=blocks)


if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
