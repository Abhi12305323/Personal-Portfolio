from pypdf import PdfReader
import os

files = [
    "12305323 cse320 mooc.pdf",
    "49_manobhiram.pdf",
    "Coursera SDMU74HHJ5MQ.pdf"
]

for f in files:
    if os.path.exists(f):
        try:
            reader = PdfReader(f)
            meta = reader.metadata
            title = meta.get('/Title', 'No Title')
            author = meta.get('/Author', 'No Author')
            print(f"File: {f}\n  Title: {title}\n  Author: {author}")
            # Also print first page text snippet to guess the course
            text = reader.pages[0].extract_text()[:200].replace('\n', ' ')
            print(f"  Snippet: {text}\n")
        except Exception as e:
            print(f"Error reading {f}: {e}")
