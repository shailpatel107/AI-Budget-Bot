<<<<<<< HEAD
from telegram import Update
from telegram.ext import ContextTypes

async def handle_text_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip().lower()

    if "add" in text:
        await update.message.reply_text("To add a transaction, use /add [amount] [category] [description]")
    elif "summary" in text:
        await update.message.reply_text("Use /summary to get a full overview of your balances.")
    elif "credit" in text:
        await update.message.reply_text("Use /credit to see your credit card usage.")
    elif "spent" in text:
        await update.message.reply_text("Use /spent [category] to check category spending.")
    else:
        await update.message.reply_text("I'm not sure what you mean — try using one of the bot commands!")
=======
def handle_text_command(update, context):
    update.message.reply_text(f"You said: {update.message.text}")
>>>>>>> 0cad325 (V2 commit)
