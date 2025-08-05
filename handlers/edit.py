
from telegram import Update
from telegram.ext import ContextTypes

async def edit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Edit command received.")

def edit(update, context):
    update.message.reply_text("Edit command triggered")

