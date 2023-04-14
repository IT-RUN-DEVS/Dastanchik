import os
import zipfile
import datetime


def backup():
    current_dir = os.getcwd() # Проверяем текущюю директорию
    desktop_dir = os.path.join(os.path.expanduser('~'), 'Desktop') # Указываем путь куда до рабочего стола
    zip_file_name = os.path.basename(current_dir) + '_' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.zip' # Даём имя файлу на основе даты когда копия была сделана
    zip_file_path = os.path.join(desktop_dir, zip_file_name) # Указываем путь к создаваемому zip файлу

    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(current_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, os.path.relpath(file_path, current_dir))

    print('Backup created at:', zip_file_path)