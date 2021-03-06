import sys
import os


def exit_cli(print_func, message):
    print_func("%s" % message)
    sys.exit(0)


def display_file(file_name):
    """
    Open given file with default user program.
    """
    if sys.platform.startswith("linux"):
        os.system("xdg-open %s" % file_name)

    elif sys.platform.startswith("darwin"):
        os.system("open %s" % file_name)
