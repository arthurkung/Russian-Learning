import os
# print (os.getcwd())
# We are in this dir:C:\Users\AK\Documents\Work\Python-project\Russian-Learning
# os. chdir("C:/Users/AK/Documents/Work/Python-project/Russian-Learning")
import zipfile
import numpy as np
import pandas as pd
import create_bible_book_list as bible
import PySimpleGUI as sg
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


# unzip and get the bible sentences into a dataframe
# unzip_file()
sentences_csv = directory_to_extract_to + '/' + unzipped_filename[0]
sentences_df = pd.read_csv(sentences_csv)

# define typing box
def typing_box():
    Russian_verse = sentences_df['russian'].iloc[0]
    English_verse = sentences_df['english'].iloc[0]
    short_verse_name = sentences_df['verse_name'].iloc[0]
    verse_full_name = bible.give_full_verse_name(short_verse_name)
    layout = [[sg.Text(verse_full_name)],[sg.Text(Russian_verse)],[sg.Text(English_verse)],
                     [sg.InputText()],
                     [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Window Title', layout)

    event, values = window.read()
    window.close()
    text_input = values[0]
    return text_input

text_input = ''

while text_input != 'stop':

    text_input = typing_box()
    sg.popup('You entered', text_input)
