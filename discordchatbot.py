import logging
#from chatterbot import ChatBot
#from chatterbot.trainers import ListTrainer
import discord, os, nmap, time, socket, subprocess, sys, datetime, psutil, random, platform, re, itertools, requests, json, asyncio
from random import randint
from subprocess import PIPE, run
from io import StringIO
from time import sleep

blocked_strings = [
    "rank",
    "+",
    "?mute",
    "?ping",
    "?help",
    "role",
    "banned",
    "muted",
    "Str",
    "Welcome",
    "startbot",
    "+startbot",
    "Enjoy your mute.",
    "!",
    "/",
    ".",
    "Hello , welcome to Horror Woods Hope you enjoy your stay :D ",
    "Your message contains a blacklisted word",
    "error: the person who asked appears to not exist.",
    "Hey , welcome to  Invites = Renegade Raider Please Read",
    "welcome  dm Space Owner to cop space, Have Fun At Space Security",
    "__What type of meme do you want to post?__",
    "You need to wait  minutes and  seconds until you can work again",
    "Hey , Welcome to TheFakeSyphex's  Among Us Discord Server",
    "Hey  Welcome to A server. That's it. Please enjoy your stay, and happy halloween🎃",
    "Hey , welcome to  Invites = Renegade Raider Please Read",
    "Hey , welcome to Bro Zone Enjoy your stay and vibe with other bros a:jiggleyosh:",
    "Have a great time here in Bro Zone",
    "nigga",
    "Nigga",
    "nigger",
    "Nigger",
    ", I've sent you the account Please check your DM",
    "`n` ■  Normie Meme",
    "__What type of meme do you want to post?__",
    "`e` ■  Edgy meme",
    "`r` ■  Repost meme",
    "`d` ■  Dank meme",
    "Your meme is __TRENDING__ with , karma. You get  coins, niceeee meme bro",
    "pls",
    "GG ,",
    ":",
    "https://",
    "http://",
    "𝕟𝕒𝕞𝕖:",
    "𝕒𝕘𝕖:",
    "𝕙𝕖𝕚𝕘𝕙𝕥:",
    "𝕕𝕠𝕓: ",
    "𝕝𝕠𝕔𝕒𝕥𝕚𝕠𝕟: ",
    "𝕤𝕖𝕩𝕦𝕒𝕝𝕚𝕥𝕪:",
    "𝕝𝕚𝕜𝕖𝕤:",
    "𝕕𝕚𝕤𝕝𝕚𝕜𝕖𝕤:",
    "Watch your language.",
    "welcome",
    "Welcome",
    "Tip",
    "found nothing to hunt",
    "$",
    "Dm",
    "interested",
    "if you are interested",
    "NetworkChuck: ",
    "Searching 🔎",
    "🎶",
    ":page_facing_up:",
    "⏩ Skipped 👍",
    "Your meme is ",
    "You went hunting ",
    "full bank account ",
    "Puring",
    "Nuking",
    "Nuked",
    "Stop spamming",
    "Banned",
    "Muted",
    "Warned",
    "Striked",
    "WANT TO WIN A RARE FORTNITE ACCOUNT",
    "has donated ",
    "you just advanced to level",
    "https://tenor.com/",
    "Handy Dandy Tip: Work hard at leveling up and you'll get rewards such as coins, items and even exclusive titles and multipliers"
]

with open("dialog.dat", "r") as f:
        text = f.read()

text = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', text, flags=re.MULTILINE)

for x in text.split('\n'):
    if x in blocked_strings:
        text = text.strip(x)

text = '\n'.join(line for line in text.splitlines() if line)

with open("dialog.dat", "w") as ff:
        ff.write(text)

input_file = open("dialog.dat", "r").read().split("\n")
dupFreeList = list(dict.fromkeys(input_file))
with open("dialog.dat", "w+") as d:
    string = str()
    for x in dupFreeList:
        string += x + "\n"
    d.write(string)


print("Dialog Building (silent) \n \nInteractive (interactive)")

global thesucc
thesucc = input("Please choose silent or interactive: ")
if thesucc != "silent" and thesucc != "interactive":
    sys.exit()
#logger = logging.getLogger();logger.setLevel(logging.CRITICAL);print("\nLogging Enabled!")
class settings:
    token = "" #PUT YOUR TOKEN HERE <<<<<
bot = discord.Client()
#chatbot = ChatBot("Temper")

class knowledge:
    anomalies = [line.rstrip('\n') for line in open("delims.dat")]

#class s:
    #null = "";s = " ";n = "\n";dialog_size = str(os.path.getsize("Dialog.dat"));sentence_size = str(os.path.getsize("sentence_tokenizer.pickle"));db_size = str(os.path.getsize("db.sqlite3"));host = socket.gethostname();dt = datetime.datetime.now();dts = f"{dt}";arch = str(platform.machine());plat = str(platform.platform());ver = str(platform.version());cpu = str(platform.processor());cpu_use = str(psutil.cpu_percent());mem = str(psutil.virtual_memory())

#trainer = ListTrainer(chatbot);print('\nSuccess\nLoading Training Data')
#trainer.train([line.rstrip('\n') for line in open("dialog.dat", "r", encoding="utf8")])
print('\nSuccess\n')
print("Message History \n===============")
@bot.event
async def on_ready():
    print('-\n[Ok] - Succesfully set status')
    await bot.change_presence(activity=discord.Game(name="Im Mark!"))
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    sleep(random.randint(2,5))
    async with message.channel.typing():
        await asyncio.sleep(random.randint(1,10))
        
    
    bError = False

    if message.content:
        parsed = message.content.replace('^', '').replace('\\', '').replace("*",'').replace("#", '').replace("<", '').replace(">", '').replace("@",'').replace("?",'').replace("0",'').replace("1",'').replace("2",'').replace("3",'').replace("4",'').replace("5",'').replace("6",'').replace("7",'').replace("8",'').replace("9",'')#pruning/parsing our input
        if thesucc == "silent":
            try:#Aknowledge and save to db.
                a = open("dialog.dat", "a", encoding="utf8");a.write(f'{parsed}\n');a.close()
            except Exception as f1:
                print("First write to mem. failed!\n"+str(f1))
                bError = True
                pass
        print("{}: {}".format(message.author, message.content))

        if thesucc == "interactive":
            if bError == False:
                try:
                    #response = str(chatbot.get_response(parsed)) #Grabbing a response then sending it back
                    r = requests.get('https://some-random-api.ml/chatbot?message='+message.content, timeout=2)
                    js = r.json()
                    response = js['response']
                    #with open("response.txt", "w") as ffff:
                        #ffff.write(response)

                    #with open("response.txt", "r") as ffff:
                        #typee = ffff.read()
                    if thesucc == "silent":
                        pass
                    else:
                        await message.channel.send(response)
                        print("MarkHelmet#2492 sent a message!".format(message.content))
                except Exception as f2:
                    print(f2)
                    print("MarkHelmet#2492: Wdym?")
                    bError = True
                    await message.channel.send('Wdym?')
                    pass

            if bError == False:
                dice = randint(1,2) # Randomized reccollection of our own response   - 2nd write to mem.
                if dice == 2 and thesucc == "silent":
                    b = open("dialog.dat","a", encoding="utf8");b.write(f'{response}\n');b.close()
            elif bError == True:
                pass       
    else:
        pass
try:
    bot.run(settings.token, bot=False)
except Exception as eee:
    print(eee)
