from time import sleep

import os
import discord
from discord.ext import commands
import datetime
from discord.utils import get

client = discord.Client(intents=discord.Intents.all())
bot = commands.Bot(command_prefix="v?",
                   case_insensitive=True,
                   intents=discord.Intents.all())


@bot.event
async def on_ready():
  print("Bot Is Ready And Online!")
  await bot.change_presence(activity=discord.Activity(
    type=discord.ActivityType.watching, name="SuperVish discord server"))


@bot.event
async def on_message(message):
  if message.channel.id == 1104285474383740988:
    await message.add_reaction('⬇️')
    await message.add_reaction('⬆️')
  if message.channel.id == 1104285452678205480:
    await message.add_reaction('⬇️')
    await message.add_reaction('⬆️')
  if message.channel.id == 1104301874426949643:
    await message.add_reaction('⬇️')
    await message.add_reaction('⬆️')
  if message.channel.id == 1104302157685076069:
    await message.add_reaction('⬇️')
    await message.add_reaction('⬆️')

  if message.channel.id == 1104302157685076069:
    await message.add_reaction('⬇️')
    await message.add_reaction('⬆️')
  if message.channel.id == 1104302157685076069:
    await message.add_reaction('⬇️')
    await message.add_reaction('⬆️')
  if message.channel.id == 1104302157685076069:
    await message.add_reaction('⬇️')
    await message.add_reaction('⬆️')
  if message.channel.id == 1104302157685076069:
    await message.add_reaction('⬇️')
    await message.add_reaction('⬆️')

  if message.author.name == "Karuta":
    if message.author.discriminator == "1280":
      if 'dropping 3 cards' in message.content:
        await message.channel.send(
          "Karuta is dropping 3 cards!! <@&1072834742489194588>",
          reference=message)
  await bot.process_commands(message)


@bot.command(pass_context=True)
@commands.check_any(commands.is_owner(),
                    commands.has_permissions(ban_members=True))
async def stat(ctx):
  await ctx.send("I am alive")


@bot.command(pass_context=True)
@commands.check_any(commands.is_owner(),
                    commands.has_permissions(ban_members=True))
async def cmds(ctx):
  await ctx.send("List of all commands")
  embhlp = discord.Embed(title="Reacto Boto help",
                         description="List of all my commands :)",
                         color=000000)
  embhlp.add_field(name="help")
  embhlp.add_field(name="stat", value="Check if bot is online or offline")
  embhlp.add_field(name="ban", value="Ban a user")
  ctx.send(embed=embhlp)


@bot.command()
async def add(ctx):
  role = discord.utils.get(ctx.author.guild.roles, name="Karuta Drop ping")
  await ctx.author.add_roles(role)
  await ctx.send("Role added to " + ctx.author.mention)


@bot.command()
async def remove_role(ctx):
  role = discord.utils.get(ctx.author.guild.roles, name="Karuta Drop ping")
  await ctx.author.remove_roles(role)
  await ctx.send("The role has been removed from " + ctx.author.mention)


@bot.event
async def on_voice_state_update(member: discord.Member, before, after):
  channel = before.channel or after.channel
  ids = [
    521705298403262465, 500388745720102962, 972533275274936401,
    482185710787624960
  ]
  if member.id in ids:
    pass
  else:
    if before.channel is None and after.channel is not None:
      role = discord.utils.get(member.guild.roles, id=1083279197218295849)
      await member.add_roles(role)
    elif before.channel is not None and after.channel is None:
      role = discord.utils.get(member.guild.roles, id=1083279197218295849)
      await member.remove_roles(role)


@bot.command(pass_context=True)
@commands.check_any(commands.is_owner(),
                    commands.has_permissions(ban_members=True))
async def ban(ctx, user: discord.Member, *, message=None):
  role = discord.utils.find(lambda r: r.id == 1127857004925431818, ctx.message.guild.roles)
  if role in user.roles:
    await ctx.send(
      "**This user is under the territory of Straw hats controlled by <@645667411609255948> I cant ban this user and you also shouldn't** \n https://tenor.com/view/luffy-gif-25493107"
    )
  else:
    if user.id != 645667411609255948:
      try:
        dm = await user.create_dm()
        await dm.send(
          "Yo! Here is the ban appel form for ScoopCast Discord server \n https://forms.gle/WKaBBKKpK3K2T6kk7 \nhttps://media.tenor.com/BPSCfGuTTWcAAAAC/good-luck.gif"
        )
      except:
        pass
      await ctx.guild.ban(user)
      channel = bot.get_channel(1068794893947899935)
      name = ctx.message.author.mention
      channel = bot.get_channel(1068794893947899935)
      name = ctx.message.author.mention
      timestamp = datetime.datetime.now()
      target = user
      embedVar1 = discord.Embed(title="Member Banned")
      embedVar1.add_field(name="banned member :white_check_mark:",
                          value=target,
                          inline=True)
      embedVar = discord.Embed(
        title="Member Banned :white_check_mark:",
        description="A member was banned from this server")
      await ctx.send(embed=embedVar1)
      # Bs
      if ctx.message.author.id == 761525905687445515:
        await ctx.send('https://tenor.com/view/eminem-shh-gif-25370887')
      # shivam
      elif ctx.message.author.id == 547700188458909706:
        await ctx.send(
          'https://media.tenor.com/N029nHYM9sMAAAAC/naruto-fight.gif')
      # rohit
      elif ctx.message.author.id == 757507712593559604:
        await ctx.send(
          'https://cdn.discordapp.com/attachments/1087391102245535765/1098588346999128095/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f727949...652f7a434c30466a45547969453051773d3d2d3734303737313037372e313561346664356236386538333261613234313136363739383639382e676966.gif'
        )
      elif ctx.message.author.id == 890895979941867561:
        await ctx.send("https://tenor.com/view/shinra-tensei-gif-19640651")
      elif ctx.message.author.id == 645667411609255948:
        await ctx.send(
          "https://media.tenor.com/ce9rYjZsMQoAAAAd/zragon-infinity-gojo.gif")
      elif ctx.message.author.id == 1039143910892654702:
        await ctx.send(
          "https://media.tenor.com/OUSKdE-QRlEAAAAC/screw-you-bye.gif")
      elif ctx.message.author.id == 730705822669209742:
        await ctx.send(
          "https://media.tenor.com/w0L40qn2ldgAAAAC/dragon-ball-z-dragon-ball-super.gif"
        )
      else:
        await ctx.send('https://media.tenor.com/9zCgefg___cAAAAC/bane-no.gif')
    else:
      await ctx.send(
        ctx.message.author.mention +
        'https://media.tenor.com/816V-5-jMbMAAAAS/jujutsu-kaisen-jujutsu-kaisen0.gif'
      )
    embedVar.add_field(name="Responsible person ", value=name, inline=False)
    embedVar.add_field(name="banned member ", value=target, inline=False)
    embedVar.add_field(name="Time ", value=timestamp, inline=False)
    embedVar.add_field(name="Reason ", value=message, inline=False)
    await channel.send(embed=embedVar)


SHOULDKICK = None
yes = 0
no = 0
channelId = None
messageId = None
USERTOKICK = None


def checkVote(Yes, No):
  kick = False
  if Yes > No:
    kick = True
    return kick
  else:
    return kick


def countReaction(msg, emoji):
  emoji = [x for x in msg.reactions if str(x.emoji) == emoji]
  return emoji[0].count


@bot.event
async def on_raw_reaction_add(ctx):
  global channelId, messageId, yes, no
  if ctx.channel_id == channelId:
    if ctx.emoji.name == "1️⃣":
      channel = bot.get_channel(channelId)
      message = await channel.fetch_message(messageId)
      reaction = get(message.reactions, emoji=ctx.emoji.name)
      yes = reaction.count
    if ctx.emoji.name == "2️⃣":
      channel = bot.get_channel(channelId)
      message = await channel.fetch_message(messageId)
      reaction = get(message.reactions, emoji=ctx.emoji.name)
      no = reaction.count


@bot.command()
@commands.check_any(commands.is_owner(), commands.has_role('Server Booster'),
                    commands.has_permissions(ban_members=True))
async def voteKick(ctx, user: discord.Member, duration):
  global channelId, messageId, yes, no, USERTOKICK, SHOULDKICK
  channelId = ctx.channel.id
  USERTOKICK = user
  time = int(duration)
  poll = discord.Embed(title="Vote Kick Poll",
                       description=f"A poll has been made to kick {user}\n"
                       f"1️⃣ Yes\n"
                       f"2️⃣ No\n"
                       f"Poll has duration of {duration} Seconds",
                       colour=discord.Color.red())
  msg = await ctx.send(embed=poll)
  messageId = msg.id
  await msg.add_reaction("1️⃣")
  await msg.add_reaction("2️⃣")
  timer = await ctx.send(f"Time Remaining: {time}")
  while time > 0:
    sleep(1)
    time -= 1
    await timer.edit(content=f"Time Remaining: {time}")
  result = discord.Embed(title="Results",
                         description=f"Yes: {yes}, No: {no}",
                         colour=discord.Color.yellow())
  await ctx.send(embed=result)
  SHOULDKICK = checkVote(yes, no)
  if SHOULDKICK:
    await user.move_to(None)
    msgkick = discord.Embed(title=f"{user} has been Kicked from the VC")
    await ctx.send(embed=msgkick)


@bot.command(pass_context=True)
@commands.check_any(commands.is_owner(),
                    commands.has_permissions(ban_members=True))
async def ben(ctx, user: discord.Member, *, message=None):
  role = discord.utils.find(lambda r: r.id == 1127857004925431818,
                            ctx.message.guild.roles)
  print(role)
  if role in user.roles:
    await ctx.send(
      "**This user is under the territory of Straw hats controlled by <@645667411609255948> I cant ban this user and you also shouldn't** \n https://tenor.com/view/luffy-gif-25493107"
    )
  else:
    if user.id != 645667411609255948:
      channel = bot.get_channel(1068794893947899935)
      name = ctx.message.author.mention
      channel = bot.get_channel(1068794893947899935)
      name = ctx.message.author.mention
      timestamp = datetime.datetime.now()
      target = user
      embedVar1 = discord.Embed(title="Member Banned")
      embedVar1.add_field(name="banned member :white_check_mark:",
                          value=target,
                          inline=True)
      embedVar = discord.Embed(
        title="Member Banned :white_check_mark:",
        description="A member was banned from this server")
      await ctx.send(embed=embedVar1)
      if ctx.message.author.id == 761525905687445515:
        await ctx.send('https://tenor.com/view/eminem-shh-gif-25370887')
      elif ctx.message.author.id == 547700188458909706:
        await ctx.send(
          'https://media.tenor.com/N029nHYM9sMAAAAC/naruto-fight.gif')
      elif ctx.message.author.id == 757507712593559604:
        await ctx.send(
          'https://cdn.discordapp.com/attachments/1087391102245535765/1098588346999128095/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f727949...652f7a434c30466a45547969453051773d3d2d3734303737313037372e313561346664356236386538333261613234313136363739383639382e676966.gif'
        )
      elif ctx.message.author.id == 890895979941867561:
        await ctx.send("https://tenor.com/view/shinra-tensei-gif-19640651")
      elif ctx.message.author.id == 645667411609255948:
        await ctx.send(
          " https://tenor.com/view/gojo-purple-kyoshiki-murasaki-hollow-technique-purple-gojo-satoru-jujutsu-kaisen-gif-20536528"
        )
      elif ctx.message.author.id == 1039143910892654702:
        await ctx.send(
          "https://media.tenor.com/ai7K4FV5RiEAAAAC/among-us-ban.gif")
      elif ctx.message.author.id == 730705822669209742:
        await ctx.send(
          "https://media.tenor.com/w0L40qn2ldgAAAAC/dragon-ball-z-dragon-ball-super.gif"
        )
      elif ctx.message.author.id == 1080197009685889025:
        await ctx.send("https://media.tenor.com/9zCgefg___cAAAAC/bane-no.gif")
      else:
        await ctx.send(
          'https://media.tenor.com/q96_L6Ajcu4AAAAM/ban-banned.gif')
      await user.move_to(None)
    else:
      await ctx.send(
        ctx.message.author.mention +
        'https://media.tenor.com/816V-5-jMbMAAAAS/jujutsu-kaisen-jujutsu-kaisen0.gif'
      )

bot.run((os.environ["dctk"]))
