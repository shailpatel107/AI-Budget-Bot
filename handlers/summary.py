from telegram import Update
from telegram.ext import ContextTypes

async def summary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Summary command received.")
