import os, shutil


def move(file_path, dest_dir):
    file_path = os.path.join(file_path)
    dest_dir = os.path.join(dest_dir)
    shutil.move(file_path, dest_dir)


move(file_path='new/main.py', dest_dir='.')