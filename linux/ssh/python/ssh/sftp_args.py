import argparse

def get_sftp_parser():
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] destination",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""
        Python implementation of Linux Command: ls
        """,
        epilog="""
        More details can be found in the project repository: https://github.com/longyangking/ssh
        """,
        conflict_handler="resolve")

    parser._optionals.title = "Options"

    parser.add_argument('-46AaCfNpqrv')
    parser.add_argument('-B', type=int, help="buffer_size")        
    parser.add_argument('-b', help="batchfile")
    parser.add_argument('-c', help="cipher")
    parser.add_argument('-D', help="sftp_server_path")
    parser.add_argument('-F', help="ssh_config")
    parser.add_argument('-i', help="identity_file")
    parser.add_argument('-J', help="destination")
    parser.add_argument('-l', help="limit")
    parser.add_argument('-o', help="ssh_option")
    parser.add_argument('-P', help="port")
    parser.add_argument('-R', help="num_requests")
    parser.add_argument('-S', help="program")
    parser.add_argument('-s', help="subsystem | sftp_server",choices=["subsystem","sftp_server"])

    return parser