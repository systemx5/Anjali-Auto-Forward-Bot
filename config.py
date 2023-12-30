from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "696033b1a9c35f0dc027f8ecfbaa9645")
      API_ID = int(getenv("API_ID", "21011056"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "6856342807:AAFxautkt3EKiVqcRWpxhvFA7923LrUhEhU")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001970031336").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
