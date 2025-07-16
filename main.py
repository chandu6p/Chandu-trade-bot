from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Handler for /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is alive and responding!")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add /start command
    app.add_handler(CommandHandler("start", start))

    # Run the bot
    app.run_polling()

if __name__ == '__main__':
    main()
