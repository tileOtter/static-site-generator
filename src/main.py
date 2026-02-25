from textnode import TextNode, TextType
from copy_files import static_directory_copy
import os
import shutil

def main():
    destination = './public/'
    source = './static/'
    if os.path.exists(destination):
        try:
            shutil.rmtree(destination)
            print(f'Removed {destination}.')
        except Exception as e:
            print(f'Error: {e}')
    else:
        print(f'Directory {destination} not found.')
        
    static_directory_copy(destination, source)

if __name__ == "__main__":
    main()