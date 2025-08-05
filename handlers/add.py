from telegram import Update
from telegram.ext import ContextTypes
from supabase_client import supabase
import datetime

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        text = update.message.text.strip().split(maxsplit=2)
        if len(text) < 3:
            await update.message.reply_text("Usage: /add [amount] [category] (optional: description)")
            return

        amount = float(text[1])
        category_name = text[2]

        # Lookup category id
        category_resp = supabase.table('categories').select('id').eq('name', category_name).limit(1).execute()
        if category_resp.error or not category_resp.data:
            await update.message.reply_text(f"Category '{category_name}' not found.")
            return

        category_id = category_resp.data[0]['id']

        # Use default account for now
        account_resp = supabase.table('accounts').select('id').eq('name', 'Everyday').limit(1).execute()
        if account_resp.error or not account_resp.data:
            await update.message.reply_text("Default account 'Everyday' not found.")
            return

        account_id = account_resp.data[0]['id']

        data = {
            'user_id': update.effective_user.id,
            'account_id': account_id,
            'category_id': category_id,
            'amount': amount,
            'date': datetime.date.today(),
            'description': None
        }

        response = supabase.table('transactions').insert(data).execute()
        if response.error:
            await update.message.reply_text(f"Error adding transaction: {response.error.message}")
            return

        await update.message.reply_text(f"Added transaction: ${amount} for {category_name}.")
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")
