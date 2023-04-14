import os


def list():
    try:
        files = os.listdir()
        for file in files:
            print(file)
    except Exception as e:
        print("Произошла ошибка при выводе списка: {str(e)}")
