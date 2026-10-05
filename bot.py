import os

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "مرحباً بك في YemenLegalAI ⚖️\n\n"
        "أنا مساعدك الذكي لصياغة الشكاوى والطلبات والعقود والمذكرات.\n\n"
        "اكتب لي ما الذي تحتاجه وسأساعدك."
    )


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    await update.message.reply_text(
        "وصلت رسالتك:\n\n"
        + text
        + "\n\n"
        "هذه نسخة تجريبية من YemenLegalAI. "
        "سنضيف الذكاء الاصطناعي في الخطوة التالية."
    )


def main():
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    webhook_url = os.environ["WEBHOOK_URL"]
    webhook_secret = os.environ["WEBHOOK_SECRET"]

    port = int(os.environ.get("PORT", "10000"))

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, message)
    )

    print("YemenLegalAI is running...")

    app.run_webhook(
        listen="0.0.0.0",
        port=port,
        url_path="telegram",
        webhook_url=f"{webhook_url}/telegram",
        secret_token=webhook_secret,
        drop_pending_updates=True,
    )


if __name__ == "__main__":
    main()
