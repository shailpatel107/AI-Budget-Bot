from telegram import Update
from telegram.ext import ContextTypes
from supabase_client import supabase

async def ruleoverride(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.effective_user.id
        args = context.args

        if not args or args[0].lower() not in ['on', 'off']:
            await update.message.reply_text("Usage: /ruleoverride on|off")
            return

        override = args[0].lower() == 'on'

        # Upsert user's override setting
        resp = supabase.table('user_settings').upsert({
            'user_id': user_id,
            'rule_override': override
        }).execute()

        if resp.error:
            await update.message.reply_text(f"Error updating rule override: {resp.error.message}")
            return

        state = "enabled" if override else "disabled"
        await update.message.reply_text(f"Budget rule override is now {state}. Please use responsibly!")
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")
