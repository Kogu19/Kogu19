from test import *
if __name__ == '__main__':
    directory = "./speeches"
    files_names = list_of_files(directory, ".txt")


    nomsenlever = remove_ext(files_names)
    print(nomsenlever)