import os
from PIL import Image
from pypdf import PdfWriter, PdfReader

def merge_cv_with_certificates():
    writer = PdfWriter()
    
    # 1. Add the original resume
    resume_path = 'resume.pdf'
    if os.path.exists(resume_path):
        reader = PdfReader(resume_path)
        for page in reader.pages:
            writer.add_page(page)
    else:
        print(f"Error: {resume_path} not found.")
        return

    # 2. Certificates to add
    certificates = [
        'Fundamentals_of_Data_Structures.png',
        'Mastering_C_Language_Foundations.png',
        'Responsive_Web_Design_Certificate.png'
    ]
    
    temp_pdfs = []
    
    try:
        for cert in certificates:
            if os.path.exists(cert):
                # Convert PNG to PDF using Pillow
                image = Image.open(cert)
                pdf_path = cert.replace('.png', '_temp.pdf')
                # Ensure RGB mode for PDF conversion
                if image.mode != 'RGB':
                    image = image.convert('RGB')
                image.save(pdf_path, "PDF", resolution=100.0)
                temp_pdfs.append(pdf_path)
                
                # Add to the merged PDF
                cert_reader = PdfReader(pdf_path)
                for page in cert_reader.pages:
                    writer.add_page(page)
            else:
                print(f"Warning: {cert} not found.")

        # 3. Save the final merged PDF
        output_path = 'resume_full.pdf'
        with open(output_path, "wb") as f:
            writer.write(f)
        print(f"Successfully created {output_path}")
        
    finally:
        # Clean up temp files
        for temp in temp_pdfs:
            if os.path.exists(temp):
                os.remove(temp)

if __name__ == "__main__":
    merge_cv_with_certificates()
