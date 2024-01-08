# app/api-service/files-api.py
from flask import Blueprint, jsonify, request, send_file
from app.models import File
from app import db

files_api = Blueprint('files_api', __name__)

@files_api.route('/list', methods=['GET'])
def get_files():
    files = File.query.all()
    return jsonify({'files': [{'id': file.id, 'filename': file.filename, 'extracted': file.extracted} for file in files]})

@files_api.route('/files', methods=['POST'])
def add_file():
    data = request.get_json()
    filename = data.get('filename')
    if filename:
        new_file = File(filename=filename, extracted=False)
        db.session.add(new_file)
        db.session.commit()
        return jsonify({'message': 'File added successfully'}), 201
    return jsonify({'error': 'Missing filename parameter'}), 400

# @files_api.route('/cur_file', methods=['POST'])
# def get_cur_file():
#     data = request.
#     cur_file = File.query.get()

# @files_api.route('/get_image')
# def get_image():
#     # Replace 'image_path.jpg' with the path to your image file
#     image_path = 'image_path.jpg'
#     return send_file(image_path, mimetype='image/jpg')