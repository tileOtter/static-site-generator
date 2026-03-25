from copy_files import static_directory_copy
from converter import generate_page_recursive
import os
import shutil
import sys

def main():

    destination = './docs/'
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = '/'
    content = './content'
    source = './static'
    template = './template.html'
    if os.path.exists(destination):
        try:
            shutil.rmtree(destination)
            print(f'Removed {destination}.')
        except Exception as e:
            print(f'Error: {e}')
    else:
        print(f'Directory {destination} not found.')

    static_directory_copy(destination, source)
    generate_page_recursive(content, template, destination, basepath)

if __name__ == "__main__":
    main()