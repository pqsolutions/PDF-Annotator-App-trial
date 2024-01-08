## Created using python 3.10 and pymupdf version 1.23.5
import fitz
import os
import json

## stores the pdf_file details
pdf_file_dict = {
    "file_path":   None,
    "file_object": None,
    "file_page_count": None
}

## function opens and stores the pdf file object and info using fitz(PyMuPDF)
##response_dict must contain pdf_file_path
def open_file(response_dict):
    global pdf_file_dict
    pdffilepath = response_dict["pdf_file_path"]
    
    pdf_file_dict["file_path"] = pdffilepath

    if not os.path.exists(pdffilepath):
        return {"extract_text_operation": False}
    
    pdf_file_dict["file_object"] = fitz.open(pdffilepath)
    pdf_file_dict["file_page_count"] = pdf_file_dict["file_object"].page_count

##resonse_dict must contain 1.normalized bbox info in the format (x_minor, y_minor, x_major, y_major)
##                          2. page_number on which the bbox is present
def return_extracted_words(response_dict):
    global pdf_file_dict
    x0_bbox, y0_bbox, x1_bbox, y1_bbox = response_dict["bbox"]
    xcen_bbox = (x0_bbox + x1_bbox) / 2
    ycen_bbox = (y0_bbox + y1_bbox) / 2 
    current_page_no = response_dict["page_no"]

    if current_page_no >= pdf_file_dict["file_page_count"]:
        return {"extract_text_operation": False}

    # Get the chosen page
    page = pdf_file_dict["file_object"].load_page(current_page_no)  
    words = page.get_text("words")  # Get words with positional information
    
    # Get the dimensions of the page
    page_rect = page.rect
    page_width = page_rect.width
    page_height = page_rect.height
    
    # Get words with positional information
    words = page.get_text("words")  
    if len(words) == 0:
        return { "extract_text_operation":False}
    
    ##choosing words that fall within the bounding box space
    selected_words = []
    for c, word in enumerate(words):
        x0, y0, x1, y1 = word[:4]
        xcen = (x0 + x1) / ( 2 * page_width)
        ycen = (y0 + y1) / ( 2 * page_height)

        if  xcen > x0_bbox and xcen < x1_bbox:
            if ycen > y0_bbox and ycen < y1_bbox:
                selected_words.append( (word,(xcen,ycen)) )
            
    if len(selected_words) == 0:
        return { "extract_text_operation":False}
    
    ## sorting words with y_center_coordinate as primary key and x_cen as secondary 
    selected_words.sort(key=lambda x: (x[1][1], x[1][0]) )
    ## creating the message selected within the bounding box using words from fitz
    newline_ycen = selected_words[0][1][1]
    selected_message = ""
    for word in selected_words:
        if abs(( newline_ycen -  word[1][1] )) > 0.001:
            selected_message += "\n"
            newline_ycen = word[1][1]
            selected_message += word[0][4] + " "
        else:
            selected_message += word[0][4] + " "

    return {"extract_text_operation": True, "selected_message":selected_message, "words":selected_words}