# Recursive function, first deletes contents of public/ directory, then copies the contents of the static directory to the public directory
import shutil
import os

def static_directory_copy(destination, source):
    os.mkdir(destination)
    source_contents = os.listdir(source)
    for item in source_contents:
        path = os.path.join(source, item)
        extended_path = os.path.join(destination, item)
        if os.path.isfile(path):
            shutil.copy(path, extended_path, follow_symlinks=True)
            print(f'Copied file {item} to: {extended_path}')
        else:
            static_directory_copy(extended_path, path)
    
