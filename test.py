import os
import re
import math


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
        noms_sans_ext = noms_sans_ext.lstrip(prefixe)
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

def create_folder():
    os.mkdir(r"C:\Users\kogul\PycharmProjects\pythonProject\pychatbot-Corentin-Kogulaan--PMP\cleaned", mode=0o777)






def convertir_fichier(dossier_entree, dossier_sortie):
    fichiers = os.listdir(dossier_entree)
    for fichier in fichiers:
        chemin_fichier_entree = os.path.join(dossier_entree, fichier)
        print(chemin_fichier_entree )
        if os.path.isdir(dossier_entree):
            with open(chemin_fichier_entree, "r", encoding='utf8') as file:
                contenu = file.read()
            contenu_min = contenu.lower()
            chemin_fichier_sortie = os.path.join(dossier_sortie, fichier)
            with open(chemin_fichier_sortie, 'w', encoding='utf8') as file:
                file.write(contenu_min)
            print(contenu_min)


def enlever_caract(chemin):
    for filename in os.listdir(chemin):
        with open(os.path.join(chemin, filename), 'r', encoding= 'utf8') as file:
            data = file.read()
            #print(data)
        fichier_sans_carac = re.sub(r"['-]", ' ', data)
        #print(fichier_sans_carac)
        with open(os.path.join(chemin, filename), 'w', encoding='utf8') as file:
            file.write(fichier_sans_carac)

def tf(text):
    mots = text.split()
    dictionnaire_mot = {}
    for mot in mots:
        if mot in dictionnaire_mot:
            dictionnaire_mot[mot] += 1
        else:
            dictionnaire_mot[mot] = 1
    return dictionnaire_mot

def calcul_tf(file_names):
    importance_mot = []
    for files in os.listdir(file_names):
        file_path = os.path.join('cleaned', files)
        with open(file_path, 'r', encoding= 'utf-8') as file:
            text = file.read()
            dictionnaire_mot = tf(text)
        importance_mot.append(dictionnaire_mot)
    return importance_mot

def calcul_idf(importance_mot):
    idf_compteur = {}
    idf = {}
    for i in range(len(importance_mot)):
        for word in importance_mot[i]:
            if word in idf_compteur:
                idf_compteur[word] += 1
            else :
                idf_compteur[word] = 1
        for mot in idf_compteur:
            idf[mot] = math.log10((len(importance_mot) / idf_compteur[mot]))
        return idf
def calcue_tf_idf(tf, idf, file_names):
    file_names = ["'"] + file_names
    tf_idf = []
    tf_idf.append(file_names)
    for word in idf:
        tst = [word]
        for row in tf:
            if word not in row:
                tst.append(0.0)
            else:
                tst.append(row[mot] * idf[mot])
        tf_idf.append(tst)
    return tf_idf