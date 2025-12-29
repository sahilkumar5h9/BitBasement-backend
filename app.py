from flask import Flask
from flask_cors import CORS
from supabase import create_client
from config import SUPABASE_URL,SUPABASE_SERVICE_KEY,SECRET_KEY

app=Flask(__name__)
CORS(app)
app.secret_key=SECRET_KEY

supabase=create_client(SUPABASE_URL,SUPABASE_SERVICE_KEY)

from routes.auth import auth_bp
from routes.passwords import password_bp

app.register_blueprint(auth_bp,url_prefix="/auth")
app.register_blueprint(password_bp,url_prefix="/passwords")

if __name__=="__main__":
    app.run(debug=True)
