import base64
import fitz
import json
import os 

class pdf_img_helper:
    def __init__(self):
        self.cur_page = 0
        self.tot_pages = 0
        self.cur_page_img = None
        self.pdf_obj = None
        
    def open_pdf_file( self, filepath ):
        try:
            self.pdf_obj = fitz.open(filepath)
        except Exception as e:
            self.pdf_obj = None
            return({"fail":str(e)})
        
        self.tot_pages = self.pdf_obj.page_count()
        return {"success":True}
        
    def convert_cur_pages_to_imgs(self):
        page = [self.cur_page]
        image = page.get_pixmap().get_image()

        # Convert the image to a base64-encoded string
        encoded_image = base64.b64encode(image.samples).decode('utf-8')
        
        self.cur_page_img = encoded_image
        

    def go_to_next_pg(self):
        if self.cur_page < self.tot_pages - 1:
            self.cur_page = self.cur_page + 1
        self.convert_cur_page_to_img( )

    def go_to_prev_pg(self):
        if self.cur_page > 0:
            self.cur_page = self.cur_page - 1
        self.convert_cur_page_to_img( )
    
    
class pdf_annotation_helper:
    def __init__(self):
        self.annotations_dict = {}

    def load_annotation(self):
        json.loads()
    
    def save_to_file( filename ):
        json.dump( os.path.join( app.config[""], filename ) )

            

    