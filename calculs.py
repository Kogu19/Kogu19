if __name__ == '__main__':
    p = 0
    L = [ 1, 2, 3, 4, 5, 8]


    val = int(input("Saisir une valeur : "))
    pos = occurence(L, val)

    if pos == -1:
        print("Il n'y a pas d'occurence")

    else:
        print("La première occurence de ", val, "se trouve à la position", pos)
#za&s