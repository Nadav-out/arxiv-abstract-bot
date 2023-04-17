import os
import re
import arxiv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv

load_dotenv()

app = App()

def extract_arxiv_id(text: str) -> str:
    match = re.search(r'https:\/\/arxiv\.org\/pdf\/(\d+\.\d+)', text)
    return match.group(1) if match else None

@app.event("app_mention")
def command_handler(body, say, logger):
    text = body['event'].get('text')
    logger.info(f"Received message: {text}")  # Add this line for debugging

    arxiv_id = extract_arxiv_id(text)
    if arxiv_id:
        paper = arxiv.query(id_list=[arxiv_id])[0]
        abstract = paper["summary"]
        say(f"Title: {paper['title']}\nAbstract: {abstract}")

if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
