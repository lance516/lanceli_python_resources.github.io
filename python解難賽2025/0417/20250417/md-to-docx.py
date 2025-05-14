# This program converts all .md files from the "md" folder
# to .docx in "docx" folder, using glob.

# Import the required modules
import os
import glob
from docx import Document

# The main program, which is converting .md files to .docx

def main():
    # read .md files from "md" folder
    md_files = glob.glob('md/*.md')

    # create "docx" folder if it doesn't exist
    os.makedirs('docx', exist_ok=True)

    # convert each .md file to .docx
    for md_file in md_files:
        # read .md file
        with open(md_file, 'r', encoding='utf-8') as f:
            text = f.read()

        # create .docx file
        docx_file = os.path.join('docx', os.path.basename(md_file).replace('.md', '.docx'))
        doc = Document()
        doc.add_paragraph(text)
        doc.save(docx_file)

if __name__ == '__main__':
    main()