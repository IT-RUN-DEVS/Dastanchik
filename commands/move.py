import os, shutil


def move(file_path, dest_dir):
    try:
        file_path = os.path.abspath(file_path)
        dest_dir = os.path.join(dest_dir)
        if os.path.isfile(file_path):
            shutil.move(file_path, dest_dir)
            print(f"Файл {os.path.basename(file_path)} успешно перемещён в папку {dest_dir}")
        else:
            print(f"Файл {file_path} не найден")

    except Exception as e:
        print(f"Ошибка при перемещении файла: {e}")

