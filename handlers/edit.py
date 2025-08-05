from telegram import Update
from telegram.ext import ContextTypes
from supabase_client import supabase

async def edit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        args = context.args
        if len(args) < 3:
            await update.message.reply_text("Usage: /edit [transaction_id] [field] [new_value]")
            return

        transaction_id = int(args[0])
        field = args[1]
        new_value = " ".join(args[2:])

        if field not in ['amount', 'category_id', 'description', 'date']:
            await update.message.reply_text(f"Cannot edit field '{field}'. Allowed fields: amount, category_id, description, date")
            return

        update_data = {}
        if field == 'amount':
            update_data['amount'] = float(new_value)
        elif field == 'category_id':
            # Optionally, allow category name here by looking up ID
            update_data['category_id'] = int(new_value)
        elif field == 'date':
            update_data['date'] = new_value
        else:
            update_data[field] = new_value

        response = supabase.table('transactions').update(update_data).eq('id', transaction_id).execute()
        if response.error:
            await update.message.reply_text(f"Error editing transaction: {response.error.message}")
            return

        await update.message.reply_text(f"Transaction {transaction_id} updated.")
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")
