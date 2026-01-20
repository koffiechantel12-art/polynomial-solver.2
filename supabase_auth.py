from supabase import create_client
import streamlit as st

@st.cache_resource
def get_supabase():
    return create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_ANON_KEY"]
    )

def sign_in(email: str, password: str):
    sb = get_supabase()
    return sb.auth.sign_in_with_password({
        "email": email,
        "password": password
    })

def sign_out():
    sb = get_supabase()
    sb.auth.sign_out()

def get_user():
    sb = get_supabase()
    return sb.auth.get_user()
