
from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Here are the commands you can use:\n"
        "- add\n"
        "- attach\n"
        "- edit\n"
        "- starting\n"
        "- transfer\n"
        "- round up on/off [account name]\n"
        "- summary\n"
        "- spent [category]\n"
        "- credit\n"
        "- raizshare\n"
        "- raizdividends\n"
        "- raizinvested [user]\n"
        "- raizwithdraw [user]\n"
        "- alerts\n"
        "- ruleoverride\n"
        "- reset\n"
        "- help\n"
    )

def help_command(update, context):
    update.message.reply_text("Help command triggered")

