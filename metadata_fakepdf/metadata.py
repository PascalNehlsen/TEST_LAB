from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import NameObject, create_string_object

def read_meta(path: str):
    with open(path, 'rb') as _in:
        pdf = PdfReader(_in)
        meta = pdf.metadata
        pages = len(pdf.pages)

    creationdate = meta.get('/CreationDate', 'N/A')
    moddate = meta.get('/ModDate', 'N/A')
    title = meta.get('/Title', 'N/A')
    subject = meta.get('/Subject', 'N/A')
    author = meta.get('/Author', 'N/A')
    creator = meta.get('/Creator', 'N/A')
    producer = meta.get('/Producer', 'N/A')

    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Subject: {subject}")
    print(f"Creator: {creator}")
    print(f"Producer: {producer}")
    print(f"Creation Date: {creationdate}")
    print(f"Modification Date: {moddate}")
    print(f"Number of Pages: {pages}")
    
    return meta

def change_meta(input_pdf: str, output_pdf: str, new_metadata: dict):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    writer.add_metadata(reader.metadata)

    for key, value in new_metadata.items():
        writer.add_metadata({NameObject(key): create_string_object(value)})
    
    for page in reader.pages:
        writer.add_page(page)

    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)
    
    print(f"New modified PDF: {output_pdf}")

if __name__ == "__main__":
    path = 'example.pdf'
    output_path = 'example_modified.pdf'

    print("Original Data:")
    original_metadata = read_meta(path)

    new_metadata = {
        '/Title': 'Unknown PDF',
        '/Author': 'Unknown User',
        '/Subject': 'Updated Subject',
        '/Creator': 'Python PDF Creator',
        '/Producer': 'Unknown Producer',
        '/CreationDate': 'D:20240919123000'
    }

    #change_meta(path, output_path, new_metadata)

    #print("\Changed Data:")
    #read_meta(output_path)
