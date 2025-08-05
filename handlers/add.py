from telegram import Update
from telegram.ext import ContextTypes
from supabase_client import supabase
import datetime

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.effective_user.id
        text = update.message.text.split(maxsplit=1)
        if len(text) < 2:
            await update.message.reply_text("Usage: /add [amount] [category] (optional: description)")
            return
        
        # Parse input
        args = text[1].split()
        amount = float(args[0])
        category_name = args[1]
        description = " ".join(args[2:]) if len(args) > 2 else None

        # Lookup category id
        category = supabase.table('categories').select('id').eq('name', category_name).single().execute()
        if category.error or not category.data:
            await update.message.reply_text(f"Category '{category_name}' not found.")
            return

        category_id = category.data['id']

        # Use default account for now (modify later to accept account)
        account = supabase.table('accounts').select('id').eq('name', 'Everyday').single().execute()
        account_id = account.data['id']

        # Insert transaction
        data = {
            'user_id': user_id,
            'account_id': account_id,
            'category_id': category_id,
            'amount': amount,
            'date': datetime.date.today(),
            'description': description
        }
        response = supabase.table('transactions').insert(data).execute()
        if response.error:
            await update.message.reply_text(f"Error adding transaction: {response.error.message}")
            return

        await update.message.reply_text(f"Added transaction: ${amount} for {category_name}.")
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")
