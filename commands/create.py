import os


def create(file_path):
    if os.path.exists(file_path):
        print('Such a file already exists')
    else:
        try:
            with open(file_path, "w") as f:
                f.write('')
                print('Your file has been created')
        except FileExistsError:
            print('An error occurred while creating the file')