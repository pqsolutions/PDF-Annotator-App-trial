# app/api-service/fields-api.py
from flask import Blueprint, jsonify, request
from app.models import Field
from app import db

fields_api = Blueprint('fields_api', __name__)

@fields_api.route('/list', methods=['GET'])
def get_fields():
    fields = Field.query.all()
    return jsonify({'fields': [{'id': field.id, 'name': field.name} for field in fields]})

@fields_api.route('/add', methods=['POST'])
def add_field():
    data = request.get_json()
    new_field_name = data.get('name')
    if new_field_name:
        new_field = Field(name=new_field_name)
        db.session.add(new_field)
        db.session.commit()
        return jsonify({'message': 'Field added successfully'}), 201
    return jsonify({'error': 'Missing name parameter'}), 400