import os
from ssh import get_ssh_parser

if __name__ == "__main__":
    parser = get_ssh_parser()
    args = parser.parse_args()  
    key_vals = args.__dict__

    print(key_vals)