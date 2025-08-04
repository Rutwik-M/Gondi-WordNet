# config.example.py

import os

ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')

class Config:
    DATABASE_URL      = os.getenv("SUPABASE_DATABASE_URL")
    LOGIN_DATABASE_URL= os.getenv("LOGIN_DATABASE_URL")
    SUPABASE_URL      = os.getenv("SUPABASE_URL")
    SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")
    SECRET_KEY        = os.getenv("SECRET_KEY")