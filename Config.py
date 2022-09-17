import os

class Config():
  #Get it from @botfather
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "5456079515:AAEecjMGbQdsLqjRjN4belJT4z3d8opQCWM")
  # Your bot updates channel username without @ or leave empty
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "https://t.me/+InuqTPmXUi0yZGE9")
  # Heroku postgres DB URL
  DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:z0JOV76zm8cOogd6vgPr@containers-us-west-88.railway.app:7271/railway")
  # get it from my.telegram.org
  APP_ID = os.environ.get("APP_ID", 17542051)
  API_HASH = os.environ.get("API_HASH", "565f17cfd9364b79135fea9d3720c272")
  # Sudo users( goto @JVToolsBot and send /id to get your id)
  SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
  SUDO_USERS.append()
  SUDO_USERS = list(set(SUDO_USERS))

class Messages():
      HELP_MSG = [
        ".",

        "**Force Subscribe**\n__Force group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.__",
        
        "**Setup**\n__First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.__",
        
        "**Commmands**\n__/ForceSubscribe - To get the current settings.\n/ForceSubscribe no/off/disable - To turn of ForceSubscribe.\n/ForceSubscribe {channel username or channel ID} - To turn on and setup the channel.\n/ForceSubscribe clear - To unmute all members who muted by me.\n/source_code - To get bot source code😍\n\nNote: /FSub is an alias of /ForceSubscribe__",
        
       "**Devloped By @porussquad**"
      ]
      SC_MSG = "**Hey [{}](tg://user?id={})**\n click on below👇 button to get my source code, for more help ask in my support group👇👇 "

      START_MSG = "**Hey [{}](tg://user?id={})**\n__I can force members to join a specific channel before writing messages in the group.\nLearn more at /help__"
