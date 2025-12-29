import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()

SUPABASE_URL=os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY=os.getenv("SUPABASE_SERVICE_KEY")
SECRET_KEY=os.getenv("SECRET_KEY")

# Generate a key once and save it securely; keep it secret
FERNET_KEY = b"YOUR_GENERATED_KEY_HERE"

# Example to generate a key (run once):
# from cryptography.fernet import Fernet
# print(Fernet.generate_key())