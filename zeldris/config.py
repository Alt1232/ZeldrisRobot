# Create a new config.py file in same dir and import, then extend this class.

class Config(object):

    LOGGER = True

    # REQUIRED

    TOKEN = "5591822076:AAHrISefs75PHySuuBK4MEa45I2-X-vsvYA"  # Take from @BotFather

    OWNER_ID = (

        "1174557449 "  # If you dont know, run the bot and do /id in your private chat with it

    )

    OWNER_USERNAME = "rqveriie"

    API_HASH = "329a9246cc001b67895fd68a85d0f867" # for purge stuffs

    API_ID = 8781248

    # RECOMMENDED

    SQLALCHEMY_DATABASE_URI = "postgresql://tcuboige:nx6zP25bryt_KY89txDNClou1CUxu0-f@isilo.db.elephantsql.com/tcuboige"  # needed for any database modules

    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist

    REDIS_URL = "redis://default:k80lYCXTcWBfW7yALd1GU0tiAtiCPzFu@redis-18191.c266.us-east-1-3.ec2.cloud.redislabs.com:18191"  # needed for afk module, get from redislab

    LOAD = []

    NO_LOAD = []

    WEBHOOK = False

    URL = None

    MONGO_URI = "mongodb://Itachi:vMl3AGWVUcHh0enN@cluster0-shard-00-00.ydoa8.mongodb.net:27017,cluster0-shard-00-01.ydoa8.mongodb.net:27017,cluster0-shard-00-02.ydoa8.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-133a3e-shard-0&authSource=admin&retryWrites=true"

    MONGO_PORT = 27017  # leave it as it is

    MONGO_DB = "Zeldris"

    # OPTIONAL

    DEV_USERS = (

        [1174557449]

    )  # List of id's (not usernames) for users which have sudo access to the bot.

    SUPPORT_USERS = (

        [1174557449]

    )  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.

    WHITELIST_USERS = (

        [1174557449 ]

    )  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.

    WHITELIST_CHATS = []

    BLACKLIST_CHATS = []

    DONATION_LINK = None  # EG, paypal

    CERT_PATH = None

    PORT = 5000

    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands

    STRICT_GBAN = True

    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!

    BAN_STICKER = None  # banhammer marie sticker

    ALLOW_EXCL = False  # DEPRECATED, USE BELOW INSTEAD! Allow ! commands as well as /

    CUSTOM_CMD = False  # Set to ('/', '!') or whatever to enable it, like ALLOW_EXCL but with more custom handler!

    API_OPENWEATHER = None  # OpenWeather API

    SPAMWATCH_API = None  # Your SpamWatch token

    WALL_API = None

    SPAMMERS = None

class Production(Config):

    LOGGER = False

class Development(Config):

    LOGGER = True
