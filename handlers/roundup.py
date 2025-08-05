from telegram import Update
from telegram.ext import ContextTypes
from supabase_client import supabase

async def roundup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        args = context.args
        if len(args) < 2:
            await update.message.reply_text("Usage: /roundup on/off [account_name]")
            return

        toggle = args[0].lower()
        account_name = args[1]

        if toggle not in ['on', 'off']:
            await update.message.reply_text("First argument must be 'on' or 'off'.")
            return

        # Here you’d update a setting in DB or memory - example below:

        # Find account
        account_resp = supabase.table('accounts').select('id').eq('name', account_name).limit(1).execute()
        if account_resp.error or not account_resp.data:
            await update.message.reply_text(f"Account '{account_name}' not found.")
            return

        # Save roundup setting (assume a table or metadata to store this)
        # This example is just a stub:
        # supabase.table('roundup_settings').upsert({'account_id': account_resp.data[0]['id'], 'enabled': toggle == 'on'}).execute()

        await update.message.reply_text(f"Roundup turned {toggle} for account '{account_name}'. (Feature logic to be implemented)")
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")
