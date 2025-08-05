from telegram import Update
from telegram.ext import ContextTypes

async def ruleoverride(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Ruleoverride command received.")
