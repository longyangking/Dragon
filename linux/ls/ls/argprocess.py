import argparse

def get_parser():
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] ... [FILE]...",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""
        Python implementation of Linux Command: ls

        List information about the FILEs (the current directory by default).
        Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.
        """,
        epilog="""
        The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
        Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).
        Binary prefixes can be used, too: KiB=K, MiB=M, and so on.

        The TIME_STYLE argument can be full-iso, long-iso, iso, locale, or +FORMAT.
        FORMAT is interpreted like in date(1).  If FORMAT is FORMAT1<newline>FORMAT2,
        then FORMAT1 applies to non-recent files and FORMAT2 to recent files.
        TIME_STYLE prefixed with 'posix-' takes effect only outside the POSIX locale.
        Also the TIME_STYLE environment variable sets the default style to use.

        Using color to distinguish file types is disabled both by default and
        with --color=never.  With --color=auto, ls emits color codes only when
        standard output is connected to a terminal.  The LS_COLORS environment
        variable can change the settings.  Use the dircolors command to set it.

        Exit status:
        0  if OK,
        1  if minor problems (e.g., cannot access subdirectory),
        2  if serious trouble (e.g., cannot access command-line argument).

        More details can be found in the project repository: https://github.com/longyangking/ls
        """,
        conflict_handler="resolve")

    parser._optionals.title = "Mandatory arguments to long options are mandatory for short options too."

    #parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
    parser.add_argument(
        '-a', '--all',
        #type=bool,
        action='store_true',
        help="do not ignore entries starting with ."
        )
    parser.add_argument(
        '-A', '--almost-all', 
        help="do not list implied . and .."
        )
    parser.add_argument(
        '--author',
        help="with -l, print the author of each file"
    )
    parser.add_argument(
        '-b', '--escape',
        help="print C-style escapes for nongraphic characters"
    )
    parser.add_argument(
        '--block-size',
        help="with -l, scale sizes by SIZE when printing them; e.g., '--block-size=M'; see SIZE format below"
    )
    parser.add_argument(
        '-B', '--ignore-backups',
        help="do not list implied entries ending with ~"
    )
    parser.add_argument(
        '-c',
        help="with -lt: sort by, and show, ctime (time of last modification of file status information); with -l: show ctime and sort by name; otherwise: sort by ctime, newest first"
    )
    parser.add_argument(
        '-C',
        help="list entries by columns"
    )
    parser.add_argument(
        '--color',
        help="colorize the output; WHEN can be 'always' (default if omitted), 'auto', or 'never'; more info below"
    )
    parser.add_argument(
        '-d', '--directory',
        help="list directories themselves, not their contents"
    )                                 
    parser.add_argument(
        '-D', '--dired',
        help="generate output designed for Emacs' dired mode"
    ) 
    parser.add_argument(
        '-f',
        help="do not sort, enable -aU, disable -ls --color"
    )
    parser.add_argument(
        '-F', '--classify',
        help="append indicator (one of */=>@|) to entries"
    )
    parser.add_argument(
        '--file-type',
        help="likewise, except do not append '*'"
    )                          
    parser.add_argument(
        '--format',
        help="across -x, commas -m, horizontal -x, long -l, single-column -1, verbose -l, vertical -C"
    )
    parser.add_argument(
        '--full-time',
        help="like -l --time-style=full-iso"
    )
    parser.add_argument(
        '-g',
        help="like -l, but do not list owner"
    )
    parser.add_argument(
        '--group-directories-first',
        help="group directories before files; can be augmented with a --sort option, but any use of --sort=none (-U) disables grouping"
    )
    parser.add_argument(
        '-G', '--no-group',
        help="in a long listing, don't print group names"
    )
    parser.add_argument(
        '-h', "--human-readable",
        help="with -l and -s, print sizes like 1K 234M 2G etc."
    )
    parser.add_argument(
        '--si',
        help="likewise, but use powers of 1000 not 1024"
    )
    parser.add_argument(
        '-H', '--dereference-command-line',
        help="follow symbolic links listed on the command line"
    )
    parser.add_argument(
        '--dereference-command-line-symlink-to-dir',
        help="follow each command line symbolic link that points to a directory"
    )
    parser.add_argument(
        '--hide',
        help="do not list implied entries matching shell PATTERN (overridden by -a or -A)"
    )
    parser.add_argument(
        '--hyperlink',
        help="hyperlink file names; WHEN can be 'always'(default if omitted), 'auto', or 'never'"
    )
    parser.add_argument(
        '--indicator-style',
        help="append indicator with style WORD to entry names: none (default), slash (-p), file-type (--file-type), classify (-F)"
    )
    parser.add_argument(
        '-i','--inode ',
        help="print the index number of each file"
    )
    parser.add_argument(
        '-I', '--ignore',
        help="do not list implied entries matching shell PATTERN"
    )
    parser.add_argument(
        '-k', '--kibibytes',
        help="default to 1024-byte blocks for disk usage; used only with -s and per directory totals"
    )     
    parser.add_argument(
        '-l',
        help="use a long listing format"
    )
    parser.add_argument(
        '-L', '--dereference',
        help="when showing file information for a symbolic link, show information for the file the link references rather than for the link itself"
    )
    parser.add_argument(
        '-m',
        help="fill width with a comma separated list of entries"
    )
    parser.add_argument(
        '-n', '--numeric-uid-gid',
        help="like -l, but list numeric user and group IDs"
    ) 
    parser.add_argument(
        '-N', '--literal',
        help="print entry names without quoting"
    )
    parser.add_argument(
        '-o',
        help="like -l, but do not list group information"
    )      
    parser.add_argument(
        '-p', #'--indicator-style',
        help="append / indicator to directories"
    )    
    parser.add_argument(
        '-q', '--hide-control-chars',
        help="print ? instead of nongraphic characters"
    )      
    parser.add_argument(
        '--show-control-chars',
        help="show nongraphic characters as-is (the default, unless program is 'ls' and output is a terminal)"
    )                   
    parser.add_argument(
        '-Q', '--quote-name',
        help="enclose entry names in double quotes"
    )
    parser.add_argument(
        '--quoting-style',
        help="use quoting style WORD for entry names: literal, locale, shell, shell-always, shell-escape, shell-escape-always, c, escape (overrides QUOTING_STYLE environment variable)"
    )
    parser.add_argument(
        '-r', '--reverse',
        help="reverse order while sorting"
    )
    parser.add_argument(
        '-R', '--recursive',
        help="list subdirectories recursively"
    )
    parser.add_argument(
        '-s', '--size',
        help="print the allocated size of each file, in blocks"
    )
    parser.add_argument(
        '-S',
        help="sort by file size, largest first"
    )
    parser.add_argument(
        '--sort',
        help="sort by WORD instead of name: none (-U), size (-S), time (-t), version (-v), extension (-X)"
    )
    parser.add_argument(
        '--time',
        help="change the default of using modification times; access time (-u): atime, access, use; change time (-c): ctime, status; birth time: birth, creation; with -l, WORD determines which time to show; with --sort=time, sort by WORD (newest first)"
    )
    parser.add_argument(
        '--time-style',
        help="time/date format with -l; see TIME_STYLE below"
    )            
    parser.add_argument(
        '-t',
        help="sort by time, newest first; see --time"
    )
    parser.add_argument(
        '-T', '--tabsize',
        help="assume tab stops at each COLS instead of 8"
    )                    
    parser.add_argument(
        '-u',
        help="with -lt: sort by, and show, access time; with -l: show access time and sort by name; otherwise: sort by access time, newest first"
    )     
    parser.add_argument(
        '-U',
        help="do not sort; list entries in directory order"
    )
    parser.add_argument(
        '-v',
        help="natural sort of (version) numbers within text"
    )                     
    parser.add_argument(
        '-w', '--width',
        help="set output width to COLS.  0 means no limit"
    )               
    parser.add_argument(
        '-x',
        help="list entries by lines instead of by columns"
    )      
    parser.add_argument(
        '-X',
        help="sort alphabetically by entry extension"
    )         
    parser.add_argument(
        '-Z', '--context',
        help="print any security context of each file"
    )  
    parser.add_argument(
        '-1',
        help="ist one file per line.  Avoid '\n' with -q or -b"
    )                
    parser.add_argument(
        '--version',
        help="output version information and exit"
    )

    return parser