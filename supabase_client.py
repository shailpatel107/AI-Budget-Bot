import os
from supabase import create_client, Client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Example helper function: get monthly spent summary for a user
def get_monthly_spent(user_id: str):
    return supabase.rpc('get_monthly_spent').execute()

# You can add more functions here for transactions, accounts, etc.
