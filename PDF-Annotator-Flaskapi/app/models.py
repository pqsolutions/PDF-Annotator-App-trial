# app/models.py
from app import db

class Fields(db.Model):
    __tablename__ = "fields_master_table"
    id = db.Column(db.Integer, primary_key=True)
    field = db.Column(db.String(255), nullable=False)

class Files(db.Model):
    __tablename__ = "files_master_table"
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    filepath = db.Column(db.String(255), nullable=False)
    extracted = db.Column(db.Boolean, default=False)