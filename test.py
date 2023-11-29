
import os
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def remove_ext(files_names):

    for files in files_names:
        noms_sans_ext = files.split('.')[0]
        print(noms_sans_ext)
    return noms_sans_ext
def remove_Nom(files_names):
    