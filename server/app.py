from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test-db")
def db_test():
    try:
        with db.engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return "<p>Database connection successful</p>"
    except Exception as e:
        return f"<p>Database connection failed: {str(e)}</p>"

if __name__ == "__main__":
    app.run(debug=True)