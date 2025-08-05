<<<<<<< HEAD
from telegram import Update
from telegram.ext import ContextTypes

async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Reset command received.")
=======
def ruleoverride(update, context):
    update.message.reply_text("Ruleoverride command triggered")

def reset(update, context):
    update.message.reply_text("Reset command triggered")
>>>>>>> 0cad325 (V2 commit)
