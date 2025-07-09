from pyrogram import Client, filters
from googletrans import Translator
from langdetect import detect
import re

api_id = int("20144930")
api_hash = "0a04d149799c0c27fba56c8e78264186"
bot_token = "7890292688:AAGYkChpC4plamOMMdkttWx_w76WqE0Ba8A"

app = Client("translator_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
translator = Translator()

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply(
        "Assalomu alaykum! 🌍\n"
        "Men tarjimon botman. Menga matn yuboring — men uni o'zbekcha, inglizcha yoki rus tiliga tarjima qilib beraman.\n"
        "Masalan:\n"
        "📥 Salom\n📤 Hello"
    )

@app.on_message(filters.text)
def translate(client, message):
    text = message.text
    text = re.sub(r'\s+', ' ', text.strip())

    if not text:
        return message.reply("Iltimos, tarjima qilish uchun matn yuboring.")

    from_lang = detect(text)
    if from_lang == "en":
        to_lang = "uz"
    elif from_lang == "ru":
        to_lang = "en"
    else:
        to_lang = "en"

    try:
        translated = translator.translate(text, dest=to_lang)
        message.reply(f"🔤 Tarjima ({from_lang} ➡ {to_lang}):\n{translated.text}")
    except Exception as e:
        message.reply("❌ Tarjima qilishda xatolik yuz berdi.")

app.run()
