from discord.ext import commands
import discord
import platform
import os
import settings
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from http import HTTPStatus

# this specifies what extensions to load when the bot starts up
startup_extensions = ["tasks", "commands"]

bot = commands.Bot(description="Helpful Plong. For personal background tasks and more.", command_prefix="!",
				   pm_help=True)


@bot.event
async def on_ready():
	print('Logged in as ' + bot.user.name + ' (ID:' + bot.user.id + ') | Connected to ' + str(
		len(bot.servers)) + ' servers | Connected to ' + str(len(set(bot.get_all_members()))) + ' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__,
																			   platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(bot.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(bot.user.id))
	print('--------')
	await bot.change_presence(game=discord.Game(name='with my life'))


class MyHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		self.send_response(HTTPStatus.OK)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		self.wfile.write(b'Hello, Python!')
		return


def run_http_server(server_class=HTTPServer, handler_class=MyHandler):
	server_address = ('localhost' if settings.PROJECT_DOMAIN is None else settings.PROJECT_DOMAIN + '.glitch.me', settings.PORT)
	httpd = server_class(server_address, handler_class)
	print("Server works on http://localhost:" + settings.PORT)
	httpd.serve_forever()


if __name__ == "__main__":
	for extension in startup_extensions:
		try:
			bot.load_extension(extension)
		except Exception as e:
			exc = '{}: {}'.format(type(e).__name__, e)
			print('Failed to load extension {}\n{}'.format(extension, exc))

	print("token: " + settings.DISCORD_BOT_TOKEN)
	run_http_server()
	bot.run(settings.DISCORD_BOT_TOKEN)
