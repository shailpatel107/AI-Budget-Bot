from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    commands = """
Available commands:
/start - Start the bot
/help - Show this help message
/add [amount] [category] - Add a transaction
/summary - Show spending summary
/attach - Attach receipt to transaction (TODO)
/edit - Edit a transaction (TODO)
/transfer - Transfer funds (TODO)
/roundup - Toggle roundup (TODO)
/alerts - Show alerts (TODO)
/raizshare - Show Raiz investment share (TODO)
/raizdividends - Add dividends (TODO)
/raizinvested - Add invested amount (TODO)
/raizwithdraw - Withdraw Raiz share (TODO)
/ruleoverride - Override budget rules (TODO)
/reset - Reset all data (TODO)
"""
    await update.message.reply_text(commands)
