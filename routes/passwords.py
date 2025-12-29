from flask import Blueprint, request, jsonify
from supabase import create_client
from config import SUPABASE_URL, SUPABASE_SERVICE_KEY, FERNET_KEY
import bcrypt
from cryptography.fernet import Fernet

password_bp = Blueprint("passwords", __name__)
supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)
fernet = Fernet(FERNET_KEY)

@password_bp.route("/add", methods=["POST"])
def add_password():
    d = request.json
    # Hash for verification if needed
    h = bcrypt.hashpw(d["password"].encode(), bcrypt.gensalt()).decode()
    # Encrypt the password
    encrypted_pw = fernet.encrypt(d["password"].encode()).decode()
    supabase.table("passwords").insert({
        "user_id": d["user_id"],
        "website": d["website"],
        "login_username": d["login_username"],
        "password_hash": h,
        "password_encrypted": encrypted_pw,
        "strength": d["strength"]
    }).execute()
    return jsonify({"msg": "saved"}), 201

@password_bp.route("/list/<user_id>", methods=["GET"])
def list_passwords(user_id):
    r = supabase.table("passwords").select(
        "id,website,login_username,password_hash,password_encrypted,strength,created_at"
    ).eq("user_id", user_id).execute()

    # Decrypt passwords before sending to frontend
    data = []
    for p in r.data:
        try:
            decrypted_pw = fernet.decrypt(p["password_encrypted"].encode()).decode()
        except:
            decrypted_pw = ""  # fallback if decryption fails
        p["password_decrypted"] = decrypted_pw
        data.append(p)

    return jsonify(data)
