from telegram import Update
from telegram.ext import ContextTypes
from supabase_client import supabase

async def raizshare(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.effective_user.id
        response = supabase.rpc('get_raiz_share', {'user_id': user_id}).execute()
        if response.error:
            await update.message.reply_text(f"Error fetching Raiz share: {response.error.message}")
            return
        share = response.data.get('share', 0)
        await update.message.reply_text(f"📈 Your Raiz investment share: {share:.2f}%")
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")

async def raizdividends(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        args = context.args
        if len(args) < 1:
            await update.message.reply_text("Usage: /raizdividends [amount]")
            return
        amount = float(args[0])
        response = supabase.rpc('add_raiz_dividends', {'amount': amount}).execute()
        if response.error:
            await update.message.reply_text(f"Error adding dividends: {response.error.message}")
            return
        await update.message.reply_text(f"💰 Added dividends: ${amount:.2f}")
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")

async def raizinvested(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        args = context.args
        if len(args) < 2:
            await update.message.reply_text("Usage: /raizinvested [user] [amount]")
            return
        user = args[0]
        amount = float(args[1])
        response = supabase.rpc('add_raiz_investment', {'user': user, 'amount': amount}).execute()
        if response.error:
            await update.message.reply_text(f"Error adding investment: {response.error.message}")
            return
        await update.message.reply_text(f"💸 Added investment of ${amount:.2f} for {user}")
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")

async def raizwithdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        args = context.args
        if len(args) < 2:
            await update.message.reply_text("Usage: /raizwithdraw [user] [amount]")
            return
        user = args[0]
        amount = float(args[1])
        response = supabase.rpc('withdraw_raiz', {'user': user, 'amount': amount}).execute()
        if response.error:
            await update.message.reply_text(f"Error withdrawing amount: {response.error.message}")
            return
        await update.message.reply_text(f"💵 Withdrawn ${amount:.2f} for {user}")
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")