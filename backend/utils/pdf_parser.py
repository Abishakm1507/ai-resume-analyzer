import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    """
    Extracts text from a PDF file.
    """
    try:
        doc = fitz.open(file_path)
        text = ""
        
        for page in doc:
            text += page.get_text()
        
        doc.close()
        return text.strip()
    
    except Exception as e:
        return f"Error reading PDF: {str(e)}"