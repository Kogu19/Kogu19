
import os
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names
#on a recuperer le noms des fichiers

liste_president = []
prefixe = "Nomination_"
ch1 = "1"
ch2 = "2"
def remove_ext(files_names):

    for files in files_names:
        noms_sans_ext = files.split('.')[0]
        noms_sans_ext = noms_sans_ext.strip(prefixe)
        noms_sans_ext = noms_sans_ext.strip(ch1)
        noms_sans_ext = noms_sans_ext.strip(ch2)
        liste_president.append(noms_sans_ext)
    print(liste_president)

#on a enlever le prefixe et le suffixe des fichiers

def correction():
    index_mot = 4
    noms_corrige = liste_president[index_mot].replace("macr",  "macron")
    print(noms_corrige)
