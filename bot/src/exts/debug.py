from disnake.ext import commands

from .util_functions import *


class DebugStuff(commands.Cog):
    """This should be self-explanatory"""

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="gitstatus")
    async def git_status(self, inter):
        """Show the output of git status"""
        commit_msg = await run_command_shell(
            "git --no-pager log --decorate=short --pretty=oneline -n1"
        )
        await inter.send(embed=inf_msg("Git Status", "```" + commit_msg + "```"))

    @commands.slash_command(name="purgesyslog")
    async def purge_syslog(self, inter):
        """Delete all existing syslogs (USE WITH CARE) (Owner only)"""
        if inter.message.author.id == self.bot.owner_id:
            purged = await run_command_shell("rm system_log* -v")
            await inter.send(
                embed=inf_msg("Syslog Purger", "We purged:\n```" + purged + "```")
            )
        else:
            await inter.send(embed=err_msg("Oops", wrong_perms("purgesyslog")))

    @disnake.ext.commands.is_owner()
    @commands.slash_command(name="ds")
    async def ds(self, inter, *, what):
        """Debug shell for the bot owner"""
        await inter.response.defer()
        what = what.replace("'", "'")
        out = await run_command_shell(f"/bin/bash -c '{what}'")
        msg = f"```{out}```"
        if len(msg) > 1023:
            link = await paste(out)
            msg = f"See output here: {link}"
        await inter.send(msg)


def setup(bot):
    print("Loading Debug extension")
    bot.add_cog(DebugStuff(bot))
    print("Done")
