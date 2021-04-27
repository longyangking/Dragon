import os
from ssh import get_sftp_parser

if __name__ == "__main__":
    parser = get_sftp_parser()
    args = parser.parse_args()  
    key_vals = args.__dict__

    print(key_vals)