def pdf_to_text(path):
    try:
        import PyPDF2
    except ImportError:
        return "PyPDF2 kurulu değil. Kurulum: pip install PyPDF2"

    text = ""
    with open(path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += (page.extract_text() or "") + "\n"
    return text