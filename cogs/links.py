import discord
from discord.ext import commands

from utils.i18n import _, locale


class Links(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @locale
    async def support(self, ctx):
        _("""Returns the official bot support server invite link.""")
        await ctx.send(self.bot.config.support)

    @commands.command()
    @locale
    async def vote(self, ctx):
        _("""Returns bot vote link.""")
        await ctx.send(self.bot.config.vote)

    @commands.command()
    @locale
    async def invite(self, ctx):
        _("""Returns bot invite link.""")
        await ctx.send(self.bot.config.invite)

    @commands.command(aliases=["kofi", "tip"])
    @locale
    async def donate(self, ctx):
        _("""Returns OverBot's ko-fi page.""")
        try:  
            embed = discord.Embed(color=discord.Color.blue())
            embed.title = _("Support OverBot")
            embed.url = self.bot.config.kofi
            guild = await self.bot.fetch_guild(self.bot.config.support_server_id)
            owner = await guild.fetch_member(self.bot.config.owner_id)
            embed.description = _(
                "Maintaining OverBot and adding new features takes up a huge "
                "portion of [{owner}]({github_profile})'s spare time. "
                "If you enjoy using OverBot you can donate a small amount "
                "to keep the project alive or just support me. **Thank you!**\n\n"
                "{kofi}"
            ).format(
                owner=str(owner),
                github_profile=self.bot.config.github["profile"],
                kofi=self.bot.config.kofi,
            )
        except Exception as e:
            await ctx.send(embed=self.bot.embed_exception(e))
        else:
            await ctx.send(embed=embed)

    @commands.command(aliases=["git"])
    @locale
    async def github(self, ctx):
        _("""Returns the bot GitHub repository.""")
        await ctx.send(self.bot.config.github["repo"])


def setup(bot):
    bot.add_cog(Links(bot))
