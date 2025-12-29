from flask import Blueprint,request,jsonify
from supabase import create_client
from config import SUPABASE_URL,SUPABASE_SERVICE_KEY
import bcrypt

password_bp=Blueprint("passwords",__name__)
supabase=create_client(SUPABASE_URL,SUPABASE_SERVICE_KEY)

@password_bp.route("/add",methods=["POST"])
def add_password():
    d=request.json
    p=d["password"]
    p=p+p[::-1]
    h=bcrypt.hashpw(p.encode(),bcrypt.gensalt()).decode()
    supabase.table("passwords").insert({
        "user_id":d["user_id"],
        "website":d["website"],
        "login_username":d["login_username"],
        "password_hash":h,
        "strength":d["strength"]
    }).execute()
    return jsonify({"msg":"saved"}),201


@password_bp.route("/list/<user_id>",methods=["GET"])
def list_passwords(user_id):
    r=supabase.table("passwords").select(
        "id,website,login_username,strength,created_at"
    ).eq("user_id",user_id).execute()
    return jsonify(r.data)
