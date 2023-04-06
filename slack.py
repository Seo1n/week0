from slack_sdk.errors import SlackApiError
from pymongo import MongoClient
import requests
from datetime import date
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bolt.adapter.flask import SlackRequestHandler
from flask import Blueprint, Flask
import ssl

# slack_bp = Blueprint('slack', __name__)

client = MongoClient('mongodb://test:test@localhost',27017)

ssl._create_default_https_context = ssl._create_unverified_context

app = App(token="xoxb-5077704286977-5062165098101-gSOe7FIKFUnUcFtDwvl6rf4X")
handler = SocketModeHandler(app_token="xapp-1-A051ZGZQDJ8-5058886934326-4ede9ed7d821c7dd9235be4ab25cbdebfc20bdd2ddb0bec672c9da42068a73f7", app=app)

db = client.jungle
cursor_all = db.users.find({})
all_data = []
for document in cursor_all:
    all_data.append(document)
all_data.sort(key=lambda x: x.get('total'),reverse=True)
number_one = all_data[0]['name']
starttime = date.today().strftime("%Y-%m-%d")
time = str(starttime)
result = time + " 의 공부시간 1위는 " + number_one

@app.event("app_mention")
def handle_mention(event, say):
    try:
        # Send a reply to the user who mentioned the bot
        say(f"<@{event['user']}> {result}")
    except Exception as e:
        print(f"Error sending message: {e}")

if __name__ == "__main__":
    handler.start()