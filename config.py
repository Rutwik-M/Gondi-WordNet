import os

class Config:
    SECRET_KEY = os.urandom(24)
    DATABASE_URL = os.getenv('SUPABASE_DATABASE_URL', 'postgresql://postgres.kcsxtvbepmdgohpnggdd:ZnyDyoH68uA3Rp87@aws-0-us-west-1.pooler.supabase.com:5432/postgres?sslmode=require')
    LOGIN_DATABASE_URL = os.getenv('LOGIN_DATABASE_URL', 'postgresql://postgres.kcsxtvbepmdgohpnggdd:ZnyDyoH68uA3Rp87@aws-0-us-west-1.pooler.supabase.com:5432/postgres?sslmode=require')
    SUPABASE_URL = os.getenv('SUPABASE_URL','https://kcsxtvbepmdgohpnggdd.supabase.co')
    SUPABASE_ANON_KEY = os.getenv('SUPABASE_ANON_KEY', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imtjc3h0dmJlcG1kZ29ocG5nZ2RkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzYyNjI5NjYsImV4cCI6MjA1MTgzODk2Nn0.n4S3GFNArGrUOwoMTCHWgWuoHRVRAJLIFj4F1xsKrm0')
