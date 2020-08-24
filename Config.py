import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "").split()))
    SUDO_USERS.append(853393439)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = "813720171:AAFD9Xz2FwGmReornUEt29UvbuAlhtufci4"
    DATABASE_URL = "postgres://rywijmqymbtxdk:a581fd6dbd457bd439aaadb7d8498497ed90ff8fae8ce15f81a65233f3cd9829@ec2-54-163-230-104.compute-1.amazonaws.com:5432/d2jt842dq8694r"
    APP_ID = "1266744"
    API_HASH = "f0db5ee8d1d0ec0ba1c288d11455529d"
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(853393439)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        "[Here](https://telegra.ph/file/d93d464a77d92dd3608de.jpg)",

        "**🔔 FORCE SUBSCRIBE :**\n\nForce Group Members To Join A Specific Channel Before Sending Messages in The Group.\nI Will Mute Members if They Not Joined Your Channel And Tell Them To Join The Channel And Unmute Themself By Pressing A Button.",
        
        "**⚙ SETUP :**\n\nFirst Of All Add Me In The Group As Admin With Ban Users Permission And In The Channel As Admin.\n● Note: Only Creator Of The Group Can Setup Me.",
        
        "**⚙ COMMMANDS :**\n\n/ForceSubscribe - To Get The Current Settings.\n/ForceSubscribe no/off/disable - To Turn Of ForceSubscribe.\n/ForceSubscribe {Channel Username} - To Turn On And Setup The Channel.\n/ForceSubscribe clear - To Unmute All Members Who Muted By Me.\n\n● Note: /FSub Is An Alias Of /ForceSubscribe",
        
        "**👨‍💻 DEVELOPED BY @AmineSoukara**"
      ]

      START_MSG = "**Hey! 👋 [{}](tg://user?id={})**\n\n● I Can Force Members To Join A Specific Channel Before Writing Messages In The Group.\n● Learn More At 👉 /help__"
