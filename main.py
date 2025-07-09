from pyrogram import Client, filters

api_id = 20144930
api_hash = "0a04d149799c0c27fba56c8e78264186"
bot_token = "7890292688:AAGYkChpC4plamOMMdkttWx_w76WqE0Ba8A"

app = Client(
    "music_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply("Assalomu alaykum! Men sizga musiqalar topishda yordam beraman 🎵")

app.run()
