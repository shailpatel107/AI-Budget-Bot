from telegram import Update
from telegram.ext import ContextTypes

async def starting(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Starting balances feature is under development. Stay tuned!"
    )
