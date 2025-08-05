from telegram import Update
from telegram.ext import ContextTypes
from supabase_client import supabase

async def transfer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        args = context.args
        if len(args) < 3:
            await update.message.reply_text("Usage: /transfer [amount] [from_account] [to_account]")
            return

        amount = float(args[0])
        from_account_name = args[1]
        to_account_name = args[2]

        from_account = supabase.table('accounts').select('id', 'balance').eq('name', from_account_name).limit(1).execute()
        to_account = supabase.table('accounts').select('id', 'balance').eq('name', to_account_name).limit(1).execute()

        if from_account.error or not from_account.data:
            await update.message.reply_text(f"Source account '{from_account_name}' not found.")
            return
        if to_account.error or not to_account.data:
            await update.message.reply_text(f"Target account '{to_account_name}' not found.")
            return

        from_data = from_account.data[0]
        to_data = to_account.data[0]

        if from_data['balance'] < amount:
            await update.message.reply_text(f"Insufficient funds in '{from_account_name}'. Current balance: {from_data['balance']}")
            return

        # Update balances
        supabase.table('accounts').update({'balance': from_data['balance'] - amount}).eq('id', from_data['id']).execute()
        supabase.table('accounts').update({'balance': to_data['balance'] + amount}).eq('id', to_data['id']).execute()

        await update.message.reply_text(f"Transferred ${amount:.2f} from '{from_account_name}' to '{to_account_name}'.")
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")
