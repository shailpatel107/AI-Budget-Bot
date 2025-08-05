from telegram import Update
from telegram.ext import ContextTypes
from supabase_client import supabase

async def attach(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        args = context.args
        if len(args) < 2:
            await update.message.reply_text("Usage: /attach [transaction_id] [receipt_url]")
            return

        transaction_id = int(args[0])
        receipt_url = args[1]

        response = supabase.table('transactions').update({'receipt_url': receipt_url}).eq('id', transaction_id).execute()
        if response.error:
            await update.message.reply_text(f"Error attaching receipt: {response.error.message}")
            return

        await update.message.reply_text(f"Receipt attached to transaction {transaction_id}.")
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")
