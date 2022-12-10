import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "12541912"))
    API_HASH = os.environ.get("API_HASH", "8f66ec9617f3a9ed18fb812418427128")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5962109094:AAHjYpuw9uOGvNQ7jAaLaJcnqTZFpjm4zKk")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQCMUaOlpIDLVkVKUiVQLhtgmov31WOAM53gVJPGZcLFFwBN-hOu98e9ZsspbcsV1_f-u8_JGYi1dGx_9ZphFLZ6xY5vkGPCJKgLQ2I0ZH2lBeaVy7jTJ2SluBPOWZuxhUxC9wliDK57r9DFQH49TAhJwZSyX3opmvIodqWyN2Fe6SQ5yAk7L-oLt2IOvZ7KNQk5pOtfNFCjshdnzLAvFeJc0rsrKgSMFusUENs7c-LzibVegK7Pk1yP26RvoNoxDVKPofX5kKDKG8yqxGxPkDeGGXODF62_2nBFDvSe44FIaesszw16t6ZDLQ51E82Rxxv8sRbVFIfcwO4d1EMrav1idLbVxAA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "freemusicgod14bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1958139332")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"#optional
