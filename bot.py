import nextcord
import nest_asyncio
nest_asyncio.apply()
from nextcord.ext import commands
from nextcord import Message
import re
from TikTokApi import TikTokApi
from dotenv import dotenv_values

config = dotenv_values(".env")

intents = nextcord.Intents.default()
intents.messages = True

TIKTOK_REGEX = r'^https?:\/\/vm\.tiktok\.com\/(\w+)\/?'

class Bot(commands.Bot):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	async def on_message(self, msg: Message):
		if self.user.id != msg.author.id:
			m = re.search(TIKTOK_REGEX, msg.content)
			reply = await msg.reply("Hold on, getting information from TikTok API")
			if bool(m):
				url = m.group(0)
				with TikTokApi() as api:
					try:
						video = api.video(url=url)
						direct = video.info()["video"]["playAddr"]
						await reply.edit(direct)
					except Exception as e:
						print(e)
						await reply.edit("A TikTok with this URL doesn't exist")

bot = Bot(command_prefix='$', intents=intents)

bot.run(config["TOKEN"])
