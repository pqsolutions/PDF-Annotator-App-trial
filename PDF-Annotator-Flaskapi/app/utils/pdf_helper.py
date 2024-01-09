import base64
import fitz
import json
import os 
import io
from PIL import Image
import app

class pdf_img_helper:
    def __init__(self, file):
        self.cur_file = file
        self.cur_page = 0
        self.tot_pages = 0
        self.cur_page_img = None
        self.pdf_obj = None

    def get_cur_page(self):
        return self.cur_page 
    
    def open_pdf_file( self ):
        try:
            self.pdf_obj = fitz.open(self.cur_file.filepath)
        except Exception as e:
            self.pdf_obj = None
            return({"fail":str(e)})
        
        self.tot_pages = self.pdf_obj.page_count
        return {"success":True, "tot_pages": self.tot_pages}
        
    def convert_cur_page_to_img(self):
        page = self.pdf_obj[self.cur_page]
        img_pixmap = page.get_pixmap()
        # Convert the Pixmap to a PIL Image
        pil_image = Image.frombytes("RGB", (img_pixmap.width, img_pixmap.height), img_pixmap.samples)

        # Encode the image as base64
        buffered = io.BytesIO()
        pil_image.save(buffered, format="JPEG")
        self.cur_page_img = base64.b64encode(buffered.getvalue()).decode('utf-8')

        return { "encoded_image": self.cur_page_img}
        

    def go_to_next_pg(self):
        if self.cur_page < self.tot_pages - 1:
            self.cur_page = self.cur_page + 1
        self.convert_cur_page_to_img( )

    def go_to_prev_pg(self):
        if self.cur_page > 0:
            self.cur_page = self.cur_page - 1
        self.convert_cur_page_to_img( )
    
    
class pdf_annotation_helper:
    def __init__(self, file):
        self.cur_file = file
        self.annotations_dict = {}

    def load_annotation(self):
        json.loads( os.path.join( app.config["ANNOT_FILES_PATH"], self.cur_file.filename ) )
    
    def save_to_file( self, filename ):
        json.dump( os.path.join( app.config["ANNOT_FILES_PATH"], self.cur_file.filename ) )    