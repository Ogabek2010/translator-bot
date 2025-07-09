import os
from pyrogram import Client, filters
from googletrans import Translator
from langdetect import detect
from spellchecker import SpellChecker

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

app = Client("translator_bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)
translator = Translator()
spell = SpellChecker()

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply(
        "👋 Salom! Men avtomatik tarjimon botman.\n\n"
        "✏️ Xabar yuboring — men uni tilini aniqlab, o‘zbek, rus va ingliz tillariga tarjima qilib beraman.\n"
        "✅ Imlo xatolarini ham to‘g‘rilab yuboraman."
    )

@app.on_message(filters.text & ~filters.command("start"))
async def translate(client, message):
    text = message.text
    try:
        lang = detect(text)
    except:
        return await message.reply("Tilni aniqlay olmadim. Iltimos, aniqroq yozing.")

    corrected_words = [spell.correction(w) for w in text.split()]
    corrected_text = " ".join(corrected_words)

    result = ""
    for target_lang in ["uz", "en", "ru"]:
        if lang != target_lang:
            translated = translator.translate(corrected_text, src=lang, dest=target_lang)
            result += f"✏️ {target_lang.upper()}:\n{translated.text}\n\n"

    await message.reply(result.strip())

app.run()import os
from pyrogram import Client, filters
from googletrans import Translator
from langdetect import detect
from spellchecker import SpellChecker

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

app = Client("translator_bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)
translator = Translator()
spell = SpellChecker()

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply(
        "👋 Salom! Men avtomatik tarjimon botman.\n\n"
        "✏️ Xabar yuboring — men uni tilini aniqlab, o‘zbek, rus va ingliz tillariga tarjima qilib beraman.\n"
        "✅ Imlo xatolarini ham to‘g‘rilab yuboraman."
    )

@app.on_message(filters.text & ~filters.command("start"))
async def translate(client, message):
    text = message.text
    try:
        lang = detect(text)
    except:
        return await message.reply("Tilni aniqlay olmadim. Iltimos, aniqroq yozing.")

    corrected_words = [spell.correction(w) for w in text.split()]
    corrected_text = " ".join(corrected_words)

    result = ""
    for target_lang in ["uz", "en", "ru"]:
        if lang != target_lang:
            translated = translator.translate(corrected_text, src=lang, dest=target_lang)
            result += f"✏️ {target_lang.upper()}:\n{translated.text}\n\n"

    await message.reply(result.strip())

app.run()
