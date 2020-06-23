import os
# print (os.getcwd())
# We are in this dir:C:\Users\AK\Documents\Work\Python-project\Russian-Learning
# os. chdir("C:/Users/AK/Documents/Work/Python-project/Russian-Learning")
import zipfile
import numpy as np
import pandas as pd
# import matplotlib

directory_to_extract_to='resource'
unzipped_filename = ['sentences (1).csv'  ,'verses.csv']

# function for Unzip file
def unzip_file():
    path_to_zip_file='resource/Russian-English-Bible.zip'
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)
    print('unzip complete')

# function for remove unzipped files
def remove_unzip_file():
    for file in unzipped_filename:
        file_path = directory_to_extract_to + '/' + file
        os.remove(file_path)
        print('This file is removed: {}'.format(file))

# unzip_file()
sentences_csv = directory_to_extract_to + '/' + unzipped_filename[0]
sentences_df = pd.read_csv(sentences_csv)

