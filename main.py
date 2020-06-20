import os
# print (os.getcwd())
# We are in this dir:C:\Users\AK\Documents\Work\Python-project\Russian-Learning
import zipfile
import pandas

# function for Unzip file
def unzip_file():
    path_to_zip_file='resource/Russian-English-Bible.zip'
    directory_to_extract_to='resource'
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)
    print('unzip complete')

# function for remove unzipped files
def remove_unzip_file():
    unzipped_filename = ['sentences (1).csv'  ,'verses.csv']
    for file in unzipped_filename:
        file_path = directory_to_extract_to + '/' + file
        os.remove(file_path)
        print('This file is removed: {}'.format(file))

unzip_file()


