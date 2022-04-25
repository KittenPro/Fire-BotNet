# Colors
yellow='\033[93m'
cyan='\033[96m'
pink='\033[95m'
green = '\033[92m'
red ='\033[91m'

# Counts
all = 0
dead = 0
alive = 0

# Modules
import pip
try:
    import tgcrypto, pyrogram
except ModuleNotFoundError:
    print(cyan + "Установка дополнений...\n")
    pip.main(['install', 'tgcrypto'])
    pip.main(['install', 'pyrogram'])
    import os, sys
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()

# Imports
import os, sys, time
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, ChatSendMediaForbidden
from pyrogram.types import Message, ChatPermissions
from pyrogram.handlers import MessageHandler
from accs import sess

# Clear
os.system('cls' if os.name == 'nt' else 'clear')

# Accounts fetch
app = sess
for _ in app:
    try:
        app[_].start()
        me = app[_].get_me()
        alive += 1
        all += 1
        print(green + f'[{acc}√] {me.first_name} - ({me.id}) started!')
    except Exception as exc:
        dead += 1
        all += 1
        print(red + f'[{acc}x] cannot start...\n({exc})')
time.sleep(2)

# Menu
while True:
    run = 666
    while run != 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(cyan + f"""
_____ _
|  ___(_)_ __ ___
| |_  | | '__/ _ \

|  _| | | | |  __/
|_|   |_|_|  \___|

____        _   _   _      _
| __ )  ___ | |_| \ | | ___| |_
|  _ \ / _ \| __|  \| |/ _ \ __|
| |_) | (_) | |_| |\  |  __/ |_
|____/ \___/ \__|_| \_|\___|\__|

[$] Working Accounts >> {alive}
[$] Dead Accounts >> {dead}
[$] All accounts >> {all}

[0] – Edit number of accounts
[1] – Change bio (all accounts)
[2] – Join chat
[3] – Leave chat
[4] – Flood to chat/private (text)
[5] – Flood to chat/private (gif)
[6] – Flood to chat/private (voice)
[7] – Flood to chat/private (photo)
[8] – Flood to chat/private (sticker)
[9] – Credits
[10] – Restart BotNet
[11] – Exit

By KittenDEV
""")
        action = input('>> ')
        if action in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
            run = 1
        else:
            print('[x] Unknown command!')
            time.sleep(1)

    # Accounts count changer
    if action == '0':
        sess_new = int(input(yellow + "Number of accounts >> "))
        accs = "from pyrogram import Client as session\nsess = {\n"
        for a in range(sess_new):
            b = a + 1
            accs += f"{b}: session('{b}'),\n"
        accs += "}"
        with open("accs.py", "w") as f:
            f.write(accs)
            f.close()
        print(green + '[√] Restarting BotNet...')
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

    # Change Bio
    if action == '1':
        newbio = input(yellow + 'New bio>> ')
        for _ in app:
            try:
                app[_].update_profile(bio=newbio)
                print(green + f'[v]  {_} changed bio')
            except:
                print(red + f'[x] {_} account cannot change bio')
        print(pink + f'[√] All accounts changed bio')
        input(green + '[*] Press ENTER to continue')

    # Join to chat
    if action == '2':
        group = input(yellow + 'Username>> ')
        for _ in app:
            try:
                app[_].join_chat(group)
                print(green + f'[v] {_} account joined to {group}')
            except:
                print(red + f'[x] {_} account cannot join to {group}')
        print(pink + f'[√] All accounts joined to {group}')
        input(cyan + '[*] Press ENTER to continue')

    # Leave from chat
    if action == '3':
        group = input(yellow + 'Username>> ')
        for _ in app:
            try:
                app[_].leave_chat(group)
                print(green + f'[v] {_} account leaved from {group}')
            except:
                print(red + f'[x] {_} account cannot leave from {group}')
        print(pink + f'[√] All accounts leaved from {group}')
        input(cyan + '[*] Press ENTER to continue')

    # Flood text
    if action == '4':
        group = input(yellow + 'Username>> ')
        text = input(yellow + 'Text>> ')
        msgs = int(input(yellow + 'Messages count (from every account)>> '))
        cooldown = int(input(yellow + 'Cooldown>> '))
        sms = 0
        for z in range(msgs):
            for _ in app:
                try:
                   app[_].send_message(group, text)
                   sms += 1
                   print(green + f'[v] {_} account sent {sms} message to {group}')
                   sleep(cooldown)
                except:
                   print(red + f'[x] {_} account cannot send message to {group}')
        print(pink + f'[√] All messages sent to {group}')
        input(cyan + '[*] Press ENTER to continue')

    # Flood gif
    if action == '5':
        print(pink + f'You must to put gif.gif to folder with BotNet!')
        group = input(yellow + 'Username>> ')
        gif = "gif.gif"
        text = input(yellow + 'Text>> ')
        msgs = int(input(yellow + 'Messages count (from every account)>> '))
        cooldown = int(input(yellow + 'Cooldown>> '))
        sms = 0
        for z in range(msgs):
            for _ in app:
                try:
                     app[_].send_animation(group, gif, caption=text)
                     sms += 1
                     print(green + f'[v] {_} account sent {sms} gif to {group}')
                     sleep(cooldown)
                except:
                        print(red + f'[x] {_} account cannot send gif to {group}')
        print(pink + f'[√] All gifs sent to {group}')
        input(cyan + '[*] Press ENTER to continue')

    # Flood gif
    if action == '6':
        print(pink + f'You must to put sound.mp3 to folder with BotNet!')
        group = input(yellow + 'Username>> ')
        voice = "sound.mp3"
        text = input(yellow + 'Text>> ')
        msgs = int(input(yellow + 'Voices count (from every account)>> '))
        cooldown = int(input(yellow + 'Cooldown>> '))
        sms = 0
        for z in range(msgs):
            for _ in app:
                try:
                     app[_].send_voice(group, voice, caption=text)
                     sms += 1
                     print(green + f'[v] {_} account sent {sms} voice to {group}')
                     sleep(cooldown)
                except:
                        print(red + f'[x] {_} account cannot send voice to {group}')
        print(pink + f'[√] All voices sent to {group}')
        input(cyan + '[*] Press ENTER to continue')

    # Flood photo
    if action == '7':
        print(pink + f'You must to put photo.jpg to folder with BotNet!')
        group = input(yellow + 'Username>> ')
        photo = "photo.jpg"
        text = input(yellow + 'Text>> ')
        msgs = int(input(yellow + 'Photos count (from every account)>> '))
        cooldown = int(input(yellow + 'Cooldown>> '))
        sms = 0
        for z in range(msgs):
            for _ in app:
                try:
                     app[_].send_photo(group, photo, caption=text)
                     sms += 1
                     print(green + f'[v] {_} account sent {sms} photo to {group}')
                     sleep(cooldown)
                except:
                        print(red + f'[x] {_} account cannot send message to {group}')
        print(pink + f'[√] All photos sent to {group} ')
        input(cyan + '[*] Press ENTER to continue')

    # Flood sticker
    if action == '8':
        group = input(yellow + 'Username>> ')
        print(pink + f'To get sticker id you must to send sticker to @idstickerbot and copy id.')
        sticker = input(yellow + 'Sticker ID>> ')
        msgs = int(input(yellow + 'Stickers count (from every account)>> '))
        cooldown = int(input(yellow + 'Cooldown>> '))
        sms = 0
        for z in range(msgs):
            for _ in app:
                try:
                     app[_].send_sticker(group, sticker)
                     sms += 1
                     print(green + f'[v] {_} account sent {sms} sticker to {group}')
                     sleep(cooldown)
                except:
                        print(red + f'[x] {_} account cannot send sticker to {group}')
        print(pink + f'[√] All messages sent to {group} ')
        input(cyan + '[*] Press ENTER to continue')

    # Credits
    if action == '9':
        print(cyan + """
_____ _
|  ___(_)_ __ ___
| |_  | | '__/ _ \
|  _| | | | |  __/
|_|   |_|_|  \___|

____        _   _   _      _
| __ )  ___ | |_| \ | | ___| |_
|  _ \ / _ \| __|  \| |/ _ \ __|
| |_) | (_) | |_| |\  |  __/ |_
|____/ \___/ \__|_| \_|\___|\__|

By KittenDEV (t.me/Kitten_Dev and github.com/KittenPro)
""")
        input(green + '[*] Press ENTER to back menu')
    if action == '10':
        print(green + '[√] Restarting BotNet...')
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

    # Exit
    if action == '11':
        print(green + "[√] Exiting...")
        quit()

# Idle
idle()