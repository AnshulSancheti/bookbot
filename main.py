from stats import *
import sys




def main():
    

    try:
        path = sys.argv[1]
        printdic(path)
    except Exception as e:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    if sys.argv == 0:
        raise Exception 


main()
