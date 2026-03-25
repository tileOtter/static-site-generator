from copy_files import static_directory_copy
from converter import generate_page_recursive
from pathlib import Path
import os
import shutil

def main():
    destination = './public/'
    source = './static/'
    content = './content'
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
    generate_page_recursive(content, template, destination)
    # recursively generate pages based on the files in content
    # generate_page('./content/index.md', './template.html', './public/index.html')

if __name__ == "__main__":
    main()