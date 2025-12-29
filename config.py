import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
FERNET_KEY = os.getenv("FERNET_KEY").encode()  # converts string to bytes
