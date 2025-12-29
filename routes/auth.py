from flask import Blueprint,request,jsonify
from supabase import create_client
from config import SUPABASE_URL,SUPABASE_SERVICE_KEY

auth_bp=Blueprint("auth",__name__)
supabase=create_client(SUPABASE_URL,SUPABASE_SERVICE_KEY)

@auth_bp.route("/signup",methods=["POST"])
def signup():
    d=request.json
    r=supabase.auth.sign_up({
        "email":d["email"],
        "password":d["password"]
    })
    return jsonify({"msg":"user created"}),201

@auth_bp.route("/login",methods=["POST"])
def login():
    d=request.json
    r=supabase.auth.sign_in_with_password({
        "email":d["email"],
        "password":d["password"]
    })
    return jsonify({
        "access_token":r.session.access_token,
        "user_id":r.user.id
    })
