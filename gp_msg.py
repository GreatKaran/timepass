#pylint:disable=E0001
from telethon import TelegramClient
from telethon.sync import events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon. tl. functions.messages import ImportChatInviteRequest
    
###python without telthon by @Phoenixop7 
#upgraded by adding telthon evil beast(@elbeastz)#dont dlt my credts plz###
f = []


api_id = 7292479
api_hash = "09167231f28146e88ecf0bb80b4e6192"
bot_token = '5365084582:AAGm49CZLGYbwm0aIBMeyGZALyGci5oOpTg'

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
name = "Evil Beast"
version = "1.0"
review = "Nice and better to use"
link = "http://t.me/elbeastz"
mod = 0
fmsg = "Nice $ Pro app $ Usefull app"
dlink = "http://t.me/elbeastz"
whitelist = []
z = ""
@client.on(events.NewMessage(incoming=True))
async def send(event):
  global whitelist, name, version, review, link, dlink, mod 
  chat = await event.get_chat()
  user = chat.username
  msg = event.text
 
  if "addwhite" in msg:
    whitelist.append(user)
  #if user in whitelist and 
  if event.text.startswith('post') and event.is_private:
    
    await client.send_message(entity=user,message="Type Name:(name 'App Name'")
    
    
  elif event.text.startswith('name') and event.is_private:
  	name = event.text[5:100]
  	await client.send_message(entity=user,message="Type version (version 'App Version')")
  	print(name)
 
  elif event.text.startswith('version') and event.is_private:
    version = event.text[8:100]
    print(version)
    await client.send_message(entity=user,message="Give link (link 'App link')' ")
    
  elif event.text.startswith('link') and event.is_private:
  	link = event.text[5:1000]
  	print(link)
  	await client.send_message(entity=user,message="Type Over review  (review 'App Review')")
  elif event.text.startswith('review') and event.is_private:
  	review = event.text[7:100]
  	print(review)
  	await client.send_message(entity=user,message="give downlaod link (dlink 'AppDownload Link')")
  	
  elif event.text.startswith('dlink') and event.is_private:
  	download_link = event.text[6:1000]
  	print(download_link)
  	await client.send_message(entity=user,message="Type number of mod features  (mod 'NumberOfMod')")
  	
  elif event.text.startswith('mod') and event.is_private:
  	mod_features = event.text[4:100]
  	mod = int(mod_features)
  	await client.send_message(entity = user, message ="Type {mod} features .each seperated with $  (good $ nice app $ userdull app) ")
  else:
       try:
       	if "$" in event.text:
       		features = event.text.split("$" )
       		x = f.append(features)
       		print(f)
       		await client.send_message(entity = user, message = "Now type 'create'")
       			
       except:
           pass

@client.on(events.NewMessage(incoming=True, pattern=r"create$"))
async def post(event):
	global whitelist, name, version, review, link, dlink, mod, fmsg,z
	chat = await event.get_chat()
	chat_id = chat.id
	mod = fmsg.split("$")
	#user = chat.username()
	#try:
	for i in mod:
		    z = z + "✅" + i + "\n"
	msgg =f"""**
  ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    🌀  {name}
    ❄️Version : {version}
    🔗`PlayStore `: [Click Here]({link}) 

▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
⭕️Overview : 
{review}
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
♻️Modded Features:
{z}
           
    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    ♦️ MØÐÐĒÐ AND RELEASED BY **@DUMPERMODS"""

	await client.send_message(entity= chat_id, message = f"**{msgg}**")
	await client.send_message(entity= chat_id, message = "Bot By @elbeastz and @Phoenixop7")
	#except:
	    #pass
#	    await client.send_message(entity = chat_id, message = "Please type all info")
print("loadin completed.....")

client.run_until_disconnected()
