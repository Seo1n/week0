from slack_sdk.errors import SlackApiError
from pymongo import MongoClient
import requests
from datetime import date
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import ssl

# slack_bp = Blueprint('slack', __name__)

client = MongoClient('localhost',27017)

ssl._create_default_https_context = ssl._create_unverified_context

app = App(token="xoxb-5077704286977-5062165098101-8z26sbagrskTCIb07NwnNrHm")
handler = SocketModeHandler(app_token="xapp-1-A051ZGZQDJ8-5063215700422-0168a2dbd5e91e6b9bb5029265dbe0588419a4aedd6a8bbc3e13a4c439c70826", app=app)

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
    

# db = client.jungle
# cursor_all = db.users.find({})
# all_data = []
# for document in cursor_all:
#     all_data.append(document)
# all_data.sort(key=lambda x: x.get('total'),reverse=True)
# number_one = all_data[0]['name']
# starttime = date.today().strftime("%Y-%m-%d")
# time = str(starttime)
# token = "xoxb-5077704286977-5062165098101-NAyggJaLDzTNZo8SBJiZ5jNK"
# channel = "#ranking-bot"
# result = time + " 의 공부시간 1위는 " + number_one

# try :
#     response = requests.post("https://slack.com/api/chat.postMessage",
#         headers={"Authorization": "Bearer "+token},
#         data={"channel": channel,"text": result})
#     print(response.text)
# except SlackApiError as e:
#     print("Error sending message: {}".format(e))
    

# app = Flask(__name__)
# # slack_app = App(token="xoxb-5077704286977-5062165098101-gSOe7FIKFUnUcFtDwvl6rf4X", token_verification_enabled=True)
# # slack_handler = SlackRequestHandler(slack_app)

# app = App(token="xoxb-5077704286977-5062165098101-gSOe7FIKFUnUcFtDwvl6rf4X")
# handler = SocketModeHandler(app)
# # slack_bp = App(token="xoxb-5077704286977-5062165098101-gSOe7FIKFUnUcFtDwvl6rf4X")
# # handler = SocketModeHandler(slack_bp,app_token="xoxe.xoxp-1-Mi0yLTUwNzc3MDQyODY5NzctNTA2NDk1NTMxNzA1OS01MDkzMjMzNzY1NTM2LTUwNjk0MjE1OTY1NzktNjdkZWI3NjhiMTg1MjI2ZTNhMDRjMDBkYTc3YTc3ZTlhZmY1YzBmNjEzMGJiNDIyNWZlNmU3MTFhMzIyYmEyYQ")


# @app.event("app_mention")
# def handle_mention(event, client, logger):
#     try:
#         # Send a reply to the user who mentioned the bot
#         response = client.chat_postMessage(
#             channel=event["#ranking-bot"],
#             text= "test",
#         )
#         logger.info(response)
#     except SlackApiError as e:
#         logger.error(f"Error sending message: {e}")
        
# if __name__ == "__main__":
#     app.run(port=3000)

#xoxb-5077704286977-5062165098101-gSOe7FIKFUnUcFtDwvl6rf4X
# 
