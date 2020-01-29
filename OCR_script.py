from PIL import Image
import pytesseract
import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
import re

folder_name = 'SCRIPT OUTPUT' 

def ocr_core(filename): #reading image content
    text = pytesseract.image_to_string(Image.open(filename), lang = 'eng+pol')
    return text

def new_dir(): #creating new folder for output files if not exist
    n_dir = os.path.join(cwd, folder_name)
    if not os.path.exists(n_dir):
        os.mkdir(n_dir)
        
def change_slashes(ocr_output): #changing OCR output to valid name format
    new_name = ocr_output.replace('/','_')
    return new_name
    
def copy_and_rename(input_file): #creating file copy with new name in output directory
    shutil.copy(input_file, output_dir + '/' + change_slashes(ocr_element) + ' ' + input_file)

def extract_name(input_tuple): #handling multiple files
    list(input_tuple)
    output_list = []
    for e in input_tuple:
        output_list.append(e.replace(slashed_cwd + '/', ''))
    return output_list

def is_valid(string): #checking format corectness of the string obtained via OCR
    return re.findall('[CN]MM/[A-Z]+/\d+/\d+', string)

cwd = os.getcwd() #current working directory
slashed_cwd = cwd.replace('\\', '/') #validating cwd format for further use

output_dir = cwd + '\\' + folder_name

ocr_element = ''

Tk().withdraw() #handling input by tkinter dialog box
files_input = askopenfilenames()
print(f'Inserted files: {files_input}')


new_dir() 

is_working = True
for element in extract_name(files_input):
        if ocr_core(element):
            ocr_element = ocr_core(element)
        else:
            print('No string detected in ' + element + '!')
        if is_valid(ocr_element):
            break
if not ocr_element:
    is_working = False
    print('No files created!')

if ocr_element:
    if is_valid(ocr_element):
        char_list = {'[' : '',']' : '','\'' : ''}
        ocr_element = str(is_valid(ocr_element)).translate(str.maketrans(char_list))
    else:
        print('String in ' + element + ' is not valid!')
        is_working = False
        print('No files created!')
       
print('String founded: ' + ocr_element)

if is_working:
    for element in extract_name(files_input):
        copy_and_rename(element)
        print(f'File {element} created in "SCRIPT OUTPUT" directory.')

input('Press enter to exit.')
        




