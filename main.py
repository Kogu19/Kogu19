from test import *
if __name__ == '__main__':
    directory = "./speeches"
    files_names = list_of_files(directory, ".txt")
    liste_president_finale = []
    liste_sans_doublons = []

    nom = remove_ext(files_names)
    print(nom)
    name = remove_doublons(nom)
    enlever(name)
    if os.path.isdir("cleaned"):
        print("Il y'a déjà un fichier cleaned qui existe")
    else:
        create_folder()
    dossier_entree = 'speeches'
    dossier_sortie = 'cleaned'
    convertir_fichier(dossier_entree, dossier_sortie)



