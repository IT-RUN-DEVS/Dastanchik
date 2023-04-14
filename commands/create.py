import os

def create(file_path):
    try:
        with open(file_path, "w") as f:
            f.write('')
    except FileExistsError:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as f:
            f.write(f'Файла {file_path} не существует, но мы создали новый')