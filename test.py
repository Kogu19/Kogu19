import os


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


# on a recuperer le noms des fichiers


def remove_ext(files_names):
    liste_president = []
    prefixe = "Nomination_"
    ch1 = "1"
    ch2 = "2"
    for files in files_names:
        noms_sans_ext = files.split('.')[0]
        noms_sans_ext = noms_sans_ext.strip(ch1)
        noms_sans_ext = noms_sans_ext.strip(ch2)
        noms_sans_ext = noms_sans_ext.strip(prefixe)
        liste_president.append(noms_sans_ext)
    return liste_president


# on a enlever le prefixe et le suffixe des fichiers


def remove_doublons(liste_president):
    liste_sans_doublons = []
    liste_sans_doublons = dict.fromkeys(liste_president)
    liste_sans_doublons = list(liste_sans_doublons.keys())
    return(liste_sans_doublons)


def enlever(nom):
    nom1 = "Chirac"
    nom2 = "Giscard dEstaing"
    nom3 = "Hollande"
    nom4 = "Macron"
    nom5 = "Mitterrand"
    nom6 = "Sarkozy"
    prenom1 = "Jack"
    prenom2 = "Valéry"
    prenom3 = "François"
    prenom4 = "Emmanuel"
    if nom1 == nom[0]:
        print(prenom1, nom1)
    if nom2 == nom[1]:
        print(prenom2, nom2)
    if nom3 == nom[2]:
        print(prenom3, nom3)
    if nom4 == nom[3]:
        print(prenom4, nom4)
    if nom5 == nom[4]:
        print(prenom3, nom5)
    if nom6 == nom[5]:
        print(prenom3, nom6)


