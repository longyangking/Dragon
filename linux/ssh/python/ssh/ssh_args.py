import argparse

def get_ssh_parser():
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] destination [command]",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""
        Python implementation of Linux Command: ls
        """,
        epilog="""
        More details can be found in the project repository: https://github.com/longyangking/ssh
        """,
        conflict_handler="resolve")

    parser._optionals.title = "Options"

    parser.add_argument('-46AaCfGgKkMNnqsTtVvXxYy') #type=bool,#action='store_true'
    parser.add_argument('-B', help="bind_interface")        
    parser.add_argument('-b', help="bind_address")
    parser.add_argument('-c', help="cipher_spec")
    parser.add_argument('-D', help="[bind_address:]port")
    parser.add_argument('-E', help="log_file")
    parser.add_argument('-e', help="escape_char")
    parser.add_argument('-F', help="configfile")
    parser.add_argument('-I', help="pkcs11")
    parser.add_argument('-i', help="identity_file")
    parser.add_argument('-J', help="[user@]host[:port]")
    parser.add_argument('-L', help="address")
    parser.add_argument('-l', help="login_name")
    parser.add_argument('-m', help="mac_spec")
    parser.add_argument('-O', help="ctl_cmd")
    parser.add_argument('-o', help="option")
    parser.add_argument('-p', help="port")
    parser.add_argument('-Q', help="query_option")
    parser.add_argument('-R', help="address")
    parser.add_argument('-S', help="ctl_path")
    parser.add_argument('-W', help="host:port")
    parser.add_argument('-w', help="local_tun[:remote_tun]")
    
    return parser