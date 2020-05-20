import os
import shutil
from dotenv import load_dotenv
from pathlib import Path

# Activate '.env' file
load_dotenv()
load_dotenv(verbose=True)
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# The Path of the directory to be sorted, read from the '.env' file
path = os.getenv("download_path")
# This populates a list with the filenames in the directory
list_ = os.listdir(path)

# Traverses every file
for file_ in list_:
    name, ext = os.path.splitext(file_)
    print(name)
    # Stores the extension type
    ext = ext[1:]
    # If it is directory, it forces the next iteration
    if ext == '':
        continue
    # If a directory with the name 'ext' exists, it moves the file to that directory
    if os.path.exists(path + '/' + ext):
        shutil.move(path + '/' + file_, path + '/' + ext + '/' + file_)
    # If the directory does not exist, it creates a new directory
    else:
        os.makedirs(path + '/' + ext)
        shutil.move(path + '/' + file_, path + '/' + ext + '/' + file_)
