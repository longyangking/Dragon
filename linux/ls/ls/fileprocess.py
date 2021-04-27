import os

def get_file_name_list(directory):
    names = os.listdir(directory)
    file_name_list = dict()
    for name in names:
        if os.path.isfile(os.path.join(directory, name)):
            file_name_list[name] = True
        else:
            file_name_list[name] = False

    return file_name_list

def show_file_list(file_name_list):
    for name, file_type in file_name_list.items():
        if file_type:
            print("\033[0m\033[37m{name}".format(name=name),end="")
        else: # Directory
            print("\033[1m\033[36m{name}".format(name=name),end="")

        print(" "*3, end="")
    print("")