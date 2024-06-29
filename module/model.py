from module import app
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.username} is Registered"
    
with app.app_context():
    db.create_all()