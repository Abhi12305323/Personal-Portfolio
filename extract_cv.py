import sys
import subprocess
import os

try:
    import pypdf
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pypdf", "-q"])
    import pypdf

pdf_path = "C:/Users/mmano/Downloads/Manobhiram_gen_CV_main_edited.pdf"
try:
    if os.path.exists(pdf_path):
        reader = pypdf.PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        with open("cv_text.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("CV successfully extracted to cv_text.txt")
    else:
        print(f"Error: PDF not found at {pdf_path}")
except Exception as e:
    print(f"Error reading PDF: {e}")
