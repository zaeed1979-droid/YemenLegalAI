
import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
SECRET = os.environ["WEBHOOK_SECRET"]

bot = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "مرحباً بك في YemenLegalAI ⚖️\n\n"
        "أنا مساعدك القانوني اليمني لصياغة الشكاوى والطلبات والعقود والمذكرات."
    )

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "وصلت رسالتك.\n\n"
        "هذه نسخة تجريبية من YemenLegalAI، وسنضيف الذكاء الاصطناعي في الخطوة التالية."
    )

bot.add_handler(CommandHandler("start", start))
bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))

app = Flask(__name__)

@app.post("/telegram")
def telegram_webhook():
    if request.headers.get("X-Telegram-Bot-Api-Secret-Token") != SECRET:
        return "Forbidden", 403

    update = Update.de_json(request.get_json(force=True), bot.bot)
    import asyncio
    asyncio.run(bot.process_update(update))
    return "OK", 200

@app.get("/")
def home():
    return "YemenLegalAI is running."
  
