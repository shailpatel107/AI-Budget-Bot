from telegram import Update
from telegram.ext import ContextTypes

async def alerts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Alerts command is not yet implemented.")
