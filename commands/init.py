import os


def init(path=None):
    if path is None:
        path = input('Введите директорию для инициализации: ')

    init_dir_path = os.path.join(path, '.init')  # создаем путь для директории .init
    if os.path.exists(os.path.join(path, '.init')):
        print(f'Директория инициализации {init_dir_path} уже существует.')
    else:
        os.mkdir(os.path.join(path, '.init'))
        print(f'Директория инициализации {init_dir_path} успешно создана.')