from app.models import Files

class files_helper:
    active_file_ids_list = []
    active_file_id = None
    active_list_index = -1
        
    def __init__(self):
        self.active_file_ids_list = [id for (id,) in Files.query.with_entities(Files.id).all()]
        self.active_file_id = self.active_file_ids_list[0]
        self.active_list_index = 0 
       
    def next_file_in_db(self):
        if len(self.active_file_ids_list) > 0:
            if self.active_file_id < self.active_file_ids_list[-1]:
                self.active_list_index += 1
                self.active_file_id = self.active_file_ids_list[self.active_list_index]            

    def prev_file_in_db(self):
        if len(self.active_file_ids_list) > 0:
            if self.active_file_id > self.active_file_ids_list[0]:
                self.active_list_index -= 1
                self.active_file_id = self.active_file_ids_list[self.active_list_index]
            
    def get_unannotated_files(self):
        self.active_file_ids_list = [id for (id,) in Files.query.filter(Files.extracted == False).with_entities(Files.id).all()]
        self.active_file_id = self.active_file_id[0]
        self.active_list_index = 0

    def get_all_files(self):
        self.active_file_ids_list = [id for (id,) in Files.query.with_entities(Files.id).all()]
        self.active_file_id = self.active_file_id[0]
        self.active_list_index = 0