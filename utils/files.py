import os
from pathlib import Path
from shutil import rmtree


def remove_dir_contents(dir_path:Path):
    try:
        contents = os.listdir(dir_path)
        for content_name in contents:
            content_path = Path.joinpath(p, content_name)
            if Path.is_file(content_path):
                os.remove(content_path)
            elif Path.is_dir(content_path):
                rmtree(content_path)
                
    except OSError as e:
        print("Error occurred while deleting files.")
    else:
        print(f'The directory "{dir_path}" is empty clean.')



def create_dir(dir_name:str, root:Path=Path.cwd(), replace_existing:bool=False):
    dir_path = root/dir_name
    try:
        Path.mkdir(dir_path)
    except FileExistsError as e:
        if replace_existing and Path.is_dir(dir_path):
            rmtree(dir_path)
            Path.mkdir(dir_path)
        else:
            print(f'The directory "{dir_path}" already exists.')
    finally:
        return dir_path
    
            