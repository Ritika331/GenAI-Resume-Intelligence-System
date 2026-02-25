from pypdf import PdfReader


def extract_text_from_pdf(file_path):
    """
    Extract text from a given PDF file path
    """
    text = ""

    try:
        reader = PdfReader(file_path)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        return text.strip()

    except Exception as e:
        print("Error reading PDF:", e)
        return None