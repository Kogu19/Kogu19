from test import *
if __name__ == '__main__':
    directory = "./speeches"
    files_names = list_of_files(directory, ".txt")
    liste_president_finale = []
    liste_sans_doublons = []

    nom = remove_ext(files_names)
    name = remove_doublons(nom)
    enlever(name)



