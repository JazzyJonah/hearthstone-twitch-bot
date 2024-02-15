from twitchio.ext import commands
import requests

from tokenSucks import getToken

# note to self: don't use self bot
class Bot(commands.Bot):
	def __init__(self):
		super().__init__(
			token=getToken(), 
			#client_id=clientSucks(), 
			#nick="JazzyJonah_", 
			prefix="!", 
			initial_channels=["jazzyjonah_"],
			logging = True
		)

	async def event_ready(self):
		print(f'Nick is {self.nick}\nUser id is | {self.user_id}')

	async def event_message(self, message):
		# print(message.author.name, message.content)
		await self.handle_commands(message)

	# @commands.command(name="hi")
	# async def hi(self, ctx: commands.Context, param=None):
	# 	print(param)
	# 	if not param or param == "󠀀":
	# 		await ctx.send("Please give a parameter")
	# 	else:
	# 		await ctx.send(param)


	# @commands.command(name="rank")
	# async def rank(self, ctx: commands.Context):
	# 	name = requests.get("https://data.ninjakiwi.com/battles2/users/9cb81682dc96aaa61b47871e5d22b426cb561bbf9d138c6e").json()["body"]["displayName"]
	# 	hom = requests.get("https://data.ninjakiwi.com/battles2/users/9cb81682dc96aaa61b47871e5d22b426cb561bbf9d138c6e/homs").json()["body"][0]
	# 	await ctx.send(f"{name} has {hom['score']} score and is at rank {hom['rank']}")




# client = Bot()
# client.run()