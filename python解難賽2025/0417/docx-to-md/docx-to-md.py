# this program converts each docx files to markdown files, docx files are in the directory "docx", and converts files in "md" folder
# and this program have to monitor the directory for new files
# and convert them to markdown files
# use os, glob,docx
# in the docx, change docx headings to markdown headings, docx subheadings to markdown subheadings etc
# change docx pargraphs to markdown pargraphs, docx lists to markdown lists, docx tables to markdown tables etc
# change docx bold to markdown bold, docx italic to markdown italic, docx underline to markdown underline etc

import os
import glob
import time
import math
from docx import Document   

# directory for docx files
docx_dir = "docx/"
# directory for markdown files
md_dir = "md/"


# function to convert one docx file to markdown file
def convert_docx_file(docx_file, md_file):
    # create a Document object
    document = Document(docx_file)
    # open the markdown file
    with open(md_file, "w") as f:
        # for each paragraph in the document
        for para in document.paragraphs:
            # if the paragraph is a heading
            if para.style.name.startswith('Heading'):
                # write the text of the paragraph to the markdown file, with a markdown heading
                f.write("#" *  int(para.style.name[-1]) + " " + para.text + "\n")
            # if the paragraph is a subheading
            elif para.style.name.startswith('Subheading'):
                # write the text of the paragraph to the markdown file, with a markdown subheading
                f.write("##" + para.text + "\n")
            else:
                # write the text of the paragraph to the markdown file
                f.write(para.text + "\n")
            
            # skip extra line
            f.write("\n")

# main function

# def main():
    
    
    
#     # convert all docx files in the directory to markdown files
#     for docx_file in glob.glob(docx_dir + "*.docx"):
#         # get the file name
#         file_name = os.path.basename(docx_file)
#         # convert the file
#         convert_docx_file(docx_file, md_dir + os.path.splitext(file_name)[0] + ".md")


if __name__ == '__main__':
    # check for new files every second
    while True:
        for docx_file in glob.glob(docx_dir + "*.docx"):
            # get the file name
            file_name = os.path.basename(docx_file)
            if not os.path.isfile(md_dir + os.path.splitext(file_name)[0] + ".md"):
                print("Founded new file " + file_name)
                print("Converting ...")
                convert_docx_file(docx_file, md_dir + os.path.splitext(file_name)[0] + ".md")
                print("Converted!")
            else:
                ## use hash to check whether the file has changed, if there are changes, convert again
                
                pass

        time.sleep(1)
        # every 180 seconds ask user whether they want to break this while function
        if math.floor(time.time()) % 180 == 0:
            user_input = input("Do you want to end monitoring? (y/n): ")
            if user_input == 'y':
                break

