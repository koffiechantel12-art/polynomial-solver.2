from supabase import Client

def add_history(supabase: Client, user_email: str, expression: str, roots: str):
   supabase.table("history").insert({
    "user_email": user_email,
    "expression": expr,
    "roots": roots
}).execute()


def get_history(supabase: Client, user_email: str | None = None):
    query = supabase.table("history").select("*").order("created_at", desc=True)

    if user_email:
        query = query.eq("user_email", user_email)

    res = query.execute()
    return res.data if res.data else []
