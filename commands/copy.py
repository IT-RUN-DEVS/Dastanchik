import os
import shutil


def copy(src_path, dest):
    try:
        file_name = os.path.basename(src_path)
        dest_path = os.path.join(dest, file_name)

        i = 1
        while os.path.exists(dest_path):
            parts = os.path.splitext(file_name)
            if len(parts) > 1:
                dest_path = os.path.join(dest, f"{parts[0]}_{i}{parts[1]}")
            else:
                dest_path = os.path.join(dest, f"{file_name}_{i}")
            i += 1
        shutil.copy(src_path, dest_path)
    except Exception as e:
        print(f"An error occurred while copying the file: {str(e)}")