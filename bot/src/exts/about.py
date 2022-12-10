from disnake.ext import commands

from .util_functions import *


class About(commands.Cog):
    """General bot stuff"""

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def source(self, inter):
        """Bot source code link"""
        await inter.send(
            "My source code lives here: https://github.com/SomethingGeneric/Gamerbot"
        )

    @commands.slash_command()
    async def license(self, inter):
        """Bot license file"""
        await inter.send(
            "My license lives here: https://github.com/SomethingGeneric/Gamerbot/-/blob/main/LICENSE",
        )

    @commands.slash_command()
    async def report(self, inter):
        """Report bot issues"""
        await inter.send(
            "You can file issues here: https://github.com/SomethingGeneric/Gamerbot/issues",
        )

    @commands.slash_command()
    async def version(self, inter):
        """Get git info"""
        commit_msg = await run_command_shell(
            "git --no-pager log --decorate=short --pretty=oneline -n1"
        )
        msg = ""
        msg += "Latest Git commit: \n"
        msg += "```" + commit_msg + "```"
        await inter.send(f"{msg}")

    @commands.slash_command()
    async def invite(self, inter):
        """Add me to another server"""
        await inter.send(
            "https://discord.com/api/oauth2/authorize?client_id=763559371628085288&permissions=1629910589175&scope=bot%20applications.commands",
        )

    @commands.slash_command()
    async def support(self, inter):
        """Get support for Gamerbot"""
        await inter.send("Join our server. :)", "https://discord.gg/j4nAea7cAs")


def setup(bot):
    print("Loading About ext.")
    bot.add_cog(About(bot))
