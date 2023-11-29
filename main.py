from test import *
if __name__ == '__main__':
    directory = "./speeches"
    files_names = list_of_files(directory, ".txt")


    remove_ext(files_names)
    correction()