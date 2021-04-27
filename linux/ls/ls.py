import os
from ls import get_file_name_list, show_file_list, get_parser

if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()  
    key_vals = args.__dict__

    file_name_list = dict()

    is_show_point = False
    if key_vals["all"]:
        file_name_list["."] = False
        file_name_list[".."] = False

    current_directory = os.getcwd()
    file_name_list = dict(file_name_list, **get_file_name_list(current_directory))

    # index, linefeed = 0, 5
    # terminal_size = os.get_terminal_size()
    # terminal_columns = terminal_size.columns
    # names = file_name_list.keys()

    # display the result

    show_file_list(file_name_list)