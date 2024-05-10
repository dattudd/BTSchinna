from BTSchinna.core.bot import Anony
from BTSchinna.core.dir import dirr
from BTSchinna.core.git import git
from BTSchinna.core.userbot import Userbot
from BTSchinna.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
