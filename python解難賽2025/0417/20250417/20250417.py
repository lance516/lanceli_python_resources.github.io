# This program converts .txt files from "txt" folder into .docx files in "docx" folder

import os
from docx import Document

# The main program
def main():
    # Create directories if they don't exist
    os.makedirs('txt', exist_ok=True)
    os.makedirs('docx', exist_ok=True)

    for filename in os.listdir('txt'):
        if filename.endswith('.txt'):
            txt_filename = os.path.join('txt', filename)
            docx_filename = os.path.join('docx', filename.replace('.txt', '.docx'))

            with open(txt_filename, 'r', encoding='utf-8') as f:
                text = f.read()

            doc = Document()
            doc.add_paragraph(text)
            doc.save(docx_filename)

if __name__ == '__main__':
    main()
