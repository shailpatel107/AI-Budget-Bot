<<<<<<< HEAD
from telegram import Update
from telegram.ext import ContextTypes

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Add command received.")
=======
def add(update, context):
    update.message.reply_text("Add command triggered")
>>>>>>> 0cad325 (V2 commit)
