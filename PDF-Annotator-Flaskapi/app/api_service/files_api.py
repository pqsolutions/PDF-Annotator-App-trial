# app/api-service/files-api.py
from flask import Blueprint, jsonify
import app
from app.models import Files
from app import db
from app.utils.files_helper import files_helper

files_api = Blueprint('files_api', __name__)

@files_api.route('/', methods=['POST'])
def prepare_files():
    app.files_list_obj = files_helper()
        
    return jsonify( {"success":True} ),201

from app.utils.pdf_helper import pdf_img_helper, pdf_annotation_helper
@files_api.route('/cur_file', methods=['POST'])
def get_cur_file():
    cur_id = app.files_list_obj.active_file_id
    cur_file = Files.query.get( cur_id )
    app.img_helper = pdf_img_helper(cur_file )
    app.annot_helper = pdf_annotation_helper( cur_file )
    open_response = app.img_helper.open_pdf_file()
    if "success" in open_response:
        tot_pages = open_response["tot_pages"]
        return jsonify({"success":True, "total_page":tot_pages }), 201
    return jsonify( {"fail":open_response["fail"]} )

@files_api.route('/next_file', methods=['POST'])
def get_next_file():
    app.files_list_obj.next_file_in_db()
    return jsonify({"success":True, "fileid": app.files_list_obj.active_file_id, "files":app.files_list_obj.active_file_ids_list}), 201    

@files_api.route('/prev_file', methods=['POST'])
def get_prev_file():
    app.files_list_obj.prev_file_in_db()
    return jsonify({"success":True}), 201    

@files_api.route('/cur_file/cur_page', methods=['POST'])
def get_cur_page():
    cur_page = app.img_helper.get_cur_page()
    encoded_image = app.img_helper.convert_cur_page_to_img()    
    return jsonify( {"success": True, "encoded_image":encoded_image, "cur_page":cur_page } ), 200

@files_api.route('/cur_file/next_page', methods=['POST'])
def get_cur_file_next_page():
    app.img_helper.go_to_next_pg()
    return jsonify( {"success":True, } )

@files_api.route('/cur_file/prev_page', methods=['POST'])
def get_cur_file_prev_page():
    app.img_helper.go_to_prev_pg()
    return jsonify( {"success":True, } )

@files_api.route('/save_file', methods=['POST'])
def save_file_annotations():
    cur_id = app.files_list_obj.get_cur_file_id()
    cur_file = Files.query.get( cur_id )
    cur_file.extracted = True
    db.commit()
    return jsonify({"success":True}), 201