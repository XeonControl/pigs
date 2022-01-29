import discord
import random
from discord.ext import commands


bot = commands.Bot(command_prefix = "=")

@bot.event
async def on_ready():
    activity = discord.Game(name="My prefix is '='", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is ready!")

@bot.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! **Your ping is {round(bot.latency * 1000)}ms**')

@bot.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ['Cry'
             'It is certain',
             'It is decidedly so',
             'Without a doubt',
             'Yes - definitely',
             'You may rely on it',
             'As I see it, yes',
             'Most likely',
             'Outlook good',
             'Yes',
             'Signs point to yes',
             'Reply hazy, try again',
             'Ask again later',
             'Better not tell you now',
             'Cannot predict now',
             'Concentrate and ask again',
             'Dont count on it',
             'My reply is no',
             'My sources say no',
             'Outlook not so good',
             'Very doubtful',
             'Fuck off',
             'Nope, Get the hell away',
             'No doubts, Yeah',
             'Whatever, I dont care', 
             'My Sources say no',
             'My Sources say yes',
             'Stop crying omg kid',
             'Please ask again dummy',
             'You stink',
             'I doubt... But youre dumb',
             'Back india kid',
             'No talk me I angy :(',
             'What?',
             'One kebab pls']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@bot.command()
async def wolf(ctx):
    responses = ['https://cdn.discordapp.com/attachments/795328568103272488/814806687449481216/Screenshot_20210225-204837_VK.jpg',
                'https://cdn.discordapp.com/attachments/818956585727426575/818961431571071036/unknown.png',
                'https://cdn.discordapp.com/attachments/793598317170655253/825362017233535016/unknown.png',
                'https://cdn.discordapp.com/attachments/819282964772421705/832525542296911912/BigIdolizedIndigobunting-size_restricted.gif',
                'https://cdn.discordapp.com/attachments/803377268558659644/830272932055351346/unknown-96.png https://cdn.discordapp.com/attachments/803377268558659644/830273552669212692/unknown.png',
                'https://cdn.discordapp.com/attachments/803377268558659644/830524639125176331/unknown.png https://cdn.discordapp.com/attachments/803377268558659644/830526678412427295/unknown.png',
                'https://cdn.discordapp.com/attachments/838805377810300948/838868773212651560/unknown.PNG',
                'https://cdn.discordapp.com/attachments/852458395717992469/856271881153413160/unknown-199.PNG']
    await ctx.send(f'{random.choice(responses)}')


@bot.command()
async def hot(ctx):
    responses = ['https://cdn.discordapp.com/attachments/793598317170655253/825349247708823552/unknown.png',
                'https://cdn.discordapp.com/attachments/793598317170655253/825348873072803860/unknown.png',
                'https://cdn.discordapp.com/attachments/819282964772421705/825474718701715466/My_Video13.mp4',
                'https://cdn.discordapp.com/attachments/812348812399214658/825314761649946624/unknown-25.png',
                'https://cdn.discordapp.com/attachments/812348812399214658/825158177237631006/unknown.png',
                'https://cdn.discordapp.com/attachments/852458395717992469/856271815123009586/unknown-66.PNG',
                'https://cdn.discordapp.com/attachments/852458395717992469/856271154964856892/unknown.png',
                'https://gyazo.com/51ce0cfd65f0c24d7755689a9c4b84ba',
                'https://cdn.discordapp.com/attachments/812348812399214658/827314240439975986/unknown.png']

    await ctx.send(f'{random.choice(responses)}')

@bot.command()
async def sf(ctx):
    responses = ['https://cdn.discordapp.com/attachments/689778578564317342/927157397917671434/unknown.png',
                'https://cdn.discordapp.com/attachments/882499336662032394/913107737951473724/unknown.png',
                'https://cdn.discordapp.com/attachments/882499336662032394/915624521971691541/unknown.png',
                'https://cdn.discordapp.com/attachments/689778578564317342/923585862770520064/unknown.png',
                'https://cdn.discordapp.com/attachments/689778578564317342/923564112317935616/unknown.png',
                'https://cdn.discordapp.com/attachments/689778578564317342/922937113769554001/Screenshot_2.png',
                'https://cdn.discordapp.com/attachments/929046343920517140/936981373493850153/SF.png',
                'https://gyazo.com/40dc2befd4d4ca7f411473da5828dd5d',
                'https://gyazo.com/48df51c757f9612d0225fddaed0fa8df',
                'https://cdn.discordapp.com/attachments/881210357010530354/917414618421411860/Screenshot_118.png']

    await ctx.send(f'{random.choice(responses)}')

bot.remove_command("help")

@bot.command()
async def help(ctx, member: discord.Member = None):
    await ctx. message.delete()
    if not member:
        member = ctx.message.author
    embed = discord.Embed(colour=discord.Colour.dark_purple(), timestamp=ctx.message.created_at,
                          title=f"My Commands")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")
    embed.add_field(name = "Wolf", value = "Sends a funny  screenshot/short clip about Wolf")
    embed.add_field(name = "Hot", value = "Sends a funny  screenshot/short clip about Hot")
    embed.add_field(name = "Clear", value = "Clears a chosen amount of messages (Requires Admin Perms)")
    embed.add_field(name = "Ping", value = "Displays your network latency")
    embed.add_field(name = "8ball", value = "Randomally answers a question (Must ask one!)")
    embed.add_field(name = "Info", value = "Shows mentioned user's info such as creation date, name etc. (If nobody was mentioned, the message author's info will be displayed).")
    embed.add_field(name = "Kick", value = "Kicks the mentioned user from the server. (Requires Admin Perms)")
    embed.add_field(name = "Ban", value = "Bans the mentioned user from the server. (Requires Admin Perms)")
    embed.add_field(name = "Server", value = "Announces when test server is open.")
    embed.add_field(name = "Help", value = "Shows the bot's command list.")
    await ctx.send(embed = embed)

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await ctx. message.delete()
    if reason==None:
      reason=" no reason provided"
    await ctx.guild.ban(member)
    await ctx.send(f'User {member.mention} has been banned for {reason}')
        
            
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await ctx. message.delete()
    if reason==None:
      reason=" no reason provided"
    await ctx.guild.kick(member)
    await ctx.send(f'User {member.mention} has been kicked for {reason}')

@bot.command(aliases=["whois"])
async def info(ctx, member: discord.Member = None):
    await ctx. message.delete()
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)

@bot.command()
async def server(ctx, member: discord.Member = None):
    await ctx. message.delete()
    if not member:
        member = ctx.message.author
    embed = discord.Embed(colour=discord.Colour.red(), timestamp=ctx.message.created_at,
                          title=f"Test Server Activity")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")
    embed.add_field(name="Test Server Is Open", value=("https://test.tankionline.com"))
    await ctx.send(embed=embed)



bot.run('OTM2OTc2NzQyMjI3MjUxMjEw.YfVBlw.caFQhxKWqeYCYXmsdmDM9ID63s0')
